#!/usr/bin/env python
# -*- coding: utf-8 -*-


# import needed libraries
import os
import pandas as pd  # type: ignore

from functools import reduce
from pandas import errors
from typing import Dict, List, Optional, Tuple

from omop2obo.utils import *


class ConceptAnnotator(object):
    """An annotator to map clinical codes to ontology terms. This workflow consists of four steps that are performed
    on data from a single clinical domain:
        1 - UMLS CUI and Semantic Type Annotation
        2 - Ontology DbXRef Mapping
        3 - Exact String Mapping to concept labels and/or synonyms
        4 - Similarity distance mapping

    Attributes:
        clinical_data: A Pandas DataFrame containing clinical data.
        ontology_dictionary: A nested dictionary containing ontology data, where outer keys are ontology identifiers
            (e.g. "hp", "mondo"), inner keys are data types (e.g. "label", "definition", "dbxref", and "synonyms").
            For each inner key, there is a third dictionary keyed by a string of that item type and with values that
            are the ontology URI for that string type.
        primary_key: A string containing the column name of the primary key.
        concept_codes: A list of column names containing concept-level codes (optional).
        concept_strings: A list of column names containing concept-level labels and synonyms (optional).
        ancestor_codes: A list of column names containing ancestor concept-level codes (optional).
        ancestor_strings: A list of column names containing ancestor concept-level labels and synonyms (optional).
        umls_cui_data: A Pandas DataFrame containing UMLS CUI data from MRCONSO.RRF.
        umls_tui_data: A Pandas DataFrame containing UMLS CUI data from MRSTY.RRF.
        source_code_map: A dictionary containing clinical vocabulary source code abbreviations.
        umls_double_merge: A bool specifying whether to merge UMLS SAB codes with OMOP source codes once or twice.
            Merging once will only align OMOP source codes to UMLS SAB, twice with take the CUIs from the first merge
            and merge them again with the full UMLS SAB set resulting in a larger set of matches. The default value
            is True, which means that the merge will be performed twice.

    Raises:
        TypeError:
            If clinical_file is not type str or if clinical_file is empty.
            If source_codes is not type str or if source_codes is empty.
            If ontology_dictionary is not type dict.
            If umls_mrconso_file is not type str or if umls_mrconso_file is empty.
            If umls_mrsty_file is not type str or if umls_mrsty_file is empty.
            if primary_key is not type str.
            if concept_codes, concept_strings, ancestor_codes, and ancestor_strings (if provided) are not type list.
        OSError:
            If the clinical_file does not exist.
            If the source_codes does not  exist.
            If umls_mrconso_file does not exist.
            If umls_mrsty_file does not exist.
    """

    def __init__(self, clinical_file: str, ontology_dictionary: Dict, primary_key: str, concept_codes: Tuple,
                 concept_strings: Tuple = None, ancestor_codes: Tuple = None, ancestor_strings: Tuple = None,
                 umls_mrconso_file: str = None, umls_mrsty_file: str = None, umls_expand: bool = True,
                 source_codes: str = None) -> None:

        print('#### GENERATING EXACT MATCH MAPPINGS ####')
        print('*** Setting up Environment')

        self.umls_double_merge: bool = umls_expand

        # vocabulary source code mapping -- not tested in testing file
        source_code = 'resources/mappings/source_code_vocab_map.csv' if source_codes is None else source_codes
        if not isinstance(source_code, str):
            raise TypeError('source_codes must be type str.')
        elif not os.path.exists(source_code):
            raise OSError('The {} file does not exist!'.format(source_code))
        elif os.stat(source_code).st_size == 0:
            raise TypeError('Input file: {} is empty'.format(source_code))
        else:
            print('Loading Clinical Vocabulary Abbreviations Map')
            self.source_code_map: Dict = {}
            with open(source_code, 'r') as f:
                for x in f.read().splitlines()[1:]:
                    row = x.split(',')
                    for i in row[1].split(' | '):
                        self.source_code_map[i] = row[0]
            f.close()

        # clinical_file
        if not isinstance(clinical_file, str):
            raise TypeError('clinical_file must be type str.')
        elif not os.path.exists(clinical_file):
            raise OSError('The {} file does not exist!'.format(clinical_file))
        elif os.stat(clinical_file).st_size == 0:
            raise TypeError('Input file: {} is empty'.format(clinical_file))
        else:
            print('Loading Clinical Data')
            try:
                self.clinical_data: pd.DataFrame = pd.read_csv(clinical_file, header=0, low_memory=False).astype(str)
            except pd.errors.ParserError:
                self.clinical_data = pd.read_csv(clinical_file, header=0, sep='\t', low_memory=False).astype(str)

        # check primary key
        if not isinstance(primary_key, str):
            raise TypeError('primary_key must be type str.')
        else:
            self.primary_key: str = primary_key

        # check for concept-level information
        if not isinstance(concept_codes, Tuple):  # type: ignore
            raise TypeError('concept_codes must be type tuple.')
        else:
            self.concept_codes: List = list(concept_codes)

        # check concept-level string input (optional)
        if concept_strings is None:
            self.concept_strings: Optional[List] = concept_strings
        else:
            if not isinstance(concept_strings, Tuple):  # type: ignore
                raise TypeError('concept_strings must be type tuple.')
            else:
                self.concept_strings = list(concept_strings)

        # check ancestor-level codes input (optional)
        if ancestor_codes is None:
            self.ancestor_codes: Optional[List] = ancestor_codes
        else:
            if not isinstance(ancestor_codes, Tuple):  # type: ignore
                raise TypeError('ancestor_codes must be type tuple.')
            else:
                self.ancestor_codes = list(ancestor_codes)

        # check ancestor-level strings input (optional)
        if ancestor_strings is None:
            self.ancestor_strings: Optional[List] = ancestor_strings
        else:
            if not isinstance(ancestor_strings, Tuple):  # type: ignore
                raise TypeError('ancestor_strings must be type tuple.')
            else:
                self.ancestor_strings = list(ancestor_strings)

        # check ontology_dictionary
        if not isinstance(ontology_dictionary, Dict):
            raise TypeError('ontology_dictionary must be type dict.')
        else:
            self.ont_dict: Dict = ontology_dictionary

        # check for UMLS MRCONSO file
        # assumption (line 154) currently filtering to only keep 'ENG' codes, remove this constraint if too specific
        if not umls_mrconso_file:
            self.umls_data: Optional[pd.DataFrame] = None
        else:
            if not isinstance(umls_mrconso_file, str):
                raise TypeError('umls_mrconso_file must be type str.')
            elif not os.path.exists(umls_mrconso_file):
                raise OSError('The {} file does not exist!'.format(umls_mrconso_file))
            elif os.stat(umls_mrconso_file).st_size == 0:
                raise TypeError('Input file: {} is empty'.format(umls_mrconso_file))
            else:
                print('Loading UMLS MRCONSO Data')
                headers = ['CUI', 'LANG', 'SAB', 'CODE']
                self.umls_cui_data = pd.read_csv(umls_mrconso_file, sep='|', names=headers, low_memory=False,
                                                 header=None, usecols=[0, 1, 11, 13]).drop_duplicates().astype(str)
                # light filtering and tidying
                df = self.umls_cui_data[(self.umls_cui_data.CODE != 'NOCODE') & (self.umls_cui_data.LANG == 'ENG')]
                self.umls_cui_data = df[['CUI', 'SAB', 'CODE']].drop_duplicates()
                self.umls_cui_data['CODE'] = self.umls_cui_data['SAB'] + ':' + self.umls_cui_data['CODE'].str.lower()
                self.umls_cui_data['CODE'] = self.umls_cui_data['CODE'].apply(
                    lambda j: ':'.join(j.split(':')[1:]) if len(j.split(':')) > 2 else j)
                self.umls_cui_data['CODE'] = normalizes_source_codes(self.umls_cui_data['CODE'].to_frame(),
                                                                     self.source_code_map)

        # check for UMLS MRSTY file
        if not umls_mrsty_file:
            self.umls_tui_data: Optional[pd.DataFrame] = None
        else:
            if not isinstance(umls_mrsty_file, str):
                raise TypeError('umls_mrsty_file must be type str.')
            elif not os.path.exists(umls_mrsty_file):
                raise OSError('The {} file does not exist!'.format(umls_mrsty_file))
            elif os.stat(umls_mrsty_file).st_size == 0:
                raise TypeError('Input file: {} is empty'.format(umls_mrsty_file))
            else:
                print('Loading UMLS MRSTY Data')
                headers = ['CUI', 'STY']
                self.umls_tui_data = pd.read_csv(umls_mrsty_file, header=None, sep='|', names=headers,
                                                 low_memory=False, usecols=[0, 3]).drop_duplicates().astype(str)

    def umls_cui_annotator(self, data: pd.DataFrame, key: str, code_level: str) -> pd.DataFrame:
        """Method maps concepts in a clinical data file to UMLS concepts and semantic types from the umls_cui_data
        and umls_tui_data Pandas DataFrames.

        Args:
            data: A Pandas DatFrame containing clinical data.
            key: A string containing the name of the primary key (i.e. CONCEPT_ID).
            code_level: A string containing the name of the source code column (i.e. CONCEPT_SOURCE_CODE).


        Returns:
           umls_cui_semtype: A Pandas DataFrame containing clinical concept ids and source codes as well as UMLS
            CUIs, source codes, and semantic types. An example of the output data is shown below:

                          CONCEPT_ID    CONCEPT_SOURCE_CODE     UMLS_CUI      UMLS_CODE           UMLS_SEM_TYPE
                    0        4331309               22653005     C0729608       22653005     Disease or Syndrome
                    1        4331309               22653005     C0729608       22653005     Disease or Syndrome
                    2       37018594         80251000119104     C4075981 80251000119104                 Finding

        """

        # reduce data to only those columns needed for merging
        clinical_ids = data[[key, code_level]].drop_duplicates()

        # merge reduced clinical concepts with umls concepts
        if self.umls_double_merge is True:
            # merge 1 - align omop source codes to umls sabs
            umls_cui_1 = clinical_ids.merge(self.umls_cui_data, how='inner', left_on=code_level, right_on='CODE')
            # merge 2 - align umls cuis from merge 1 to cuis in full umls (this adds additional sabs not found in omop)
            umls_cui_2 = umls_cui_1[[key, code_level, 'CUI']].merge(self.umls_cui_data, how='left', on='CUI')
            umls_cui = pd.concat([umls_cui_1, umls_cui_2])
        else:
            umls_cui = clinical_ids.merge(self.umls_cui_data, how='inner', left_on=code_level, right_on='CODE')

        umls_cui_semtype = umls_cui.merge(self.umls_tui_data, how='left', on='CUI').drop_duplicates()

        # update column names
        umls_cui_semtype.columns = [key, code_level, 'UMLS_CUI', 'UMLS_SAB', 'UMLS_CODE', 'UMLS_SEM_TYPE']

        return umls_cui_semtype

    def dbxref_mapper(self, data: pd.DataFrame, primary_key: str, code_type: str) -> pd.DataFrame:
        """Takes a stacked Pandas DataFrame and merges it with a Pandas DataFrame version of the
        ontology_dictionary_object.

            INPUT (ignore all columns starting with "UMLS" if UMLS data is not provided):
                      CONCEPT_ID            CODE          CODE_COLUMN
                0        4331309        22653005  CONCEPT_SOURCE_CODE
                1       37018594  80251000119104  CONCEPT_SOURCE_CODE
                2         442264        68172002  CONCEPT_SOURCE_CODE

            OUTPUT:
                    CONCEPT_ID      CODE          CODE_COLUMN           DBXREF    ONT   ONT_URI          EVIDENCE
                0       442264  68172002  CONCEPT_SOURCE_CODE   SCTID:68172002  MONDO       URL      DbXRef_SCTID
                1       442264  68172002            UMLS_CODE   SCTID:68172002  MONDO       URL      DbXRef_SCTID
                2      4029098 237913008  CONCEPT_SOURCE_CODE  SCTID:237913008  MONDO       URL      DbXRef_SCTID
        Args:
            data: A stacked Pandas DataFrame containing output from the umls_cui_annotator method (see INPUT above).
            primary_key: A string containing the name of the primary key (i.e. CONCEPT_ID).
            code_type: A string containing the concept_level (i.e. concept or ancestor).

        Returns:
            merged_dbxrefs: A stacked Pandas DataFrame containing ontology dbxref merging results (see OUTPUT above).
        """

        col_lab = code_type.upper() + '_DBXREF_ONT_'  # column labels
        ont_labels = merge_dictionaries(self.ont_dict, 'label', reverse=True)

        # convert ontology dictionary to Pandas DataFrame
        ont_df = pd.concat([pd.DataFrame(self.ont_dict[ont]['dbxref'].items(), columns=['CODE', col_lab + 'URI'])
                            for ont in self.ont_dict.keys() if len(self.ont_dict[ont]['dbxref']) > 0])
        # normalize source_code prefix values
        ont_df['CODE'] = normalizes_source_codes(ont_df['CODE'].to_frame(), self.source_code_map)
        # merge ontology data and clinical data and run ohdsi ananke approach to specifically pull umls ont mappings
        if self.umls_cui_data is not None:
            dbxrefs = pd.concat(
                [data.merge(ont_df, how='inner', on='CODE').drop_duplicates(),
                 ohdsi_ananke(primary_key, list(self.ont_dict.keys()), ont_df.copy(), data, self.umls_cui_data.copy())]
            )
        else:
            dbxrefs = data.merge(ont_df, how='inner', on='CODE').drop_duplicates()

        # update content and labels
        dbxrefs[col_lab + 'TYPE'] = dbxrefs[col_lab + 'URI'].apply(lambda x: x.split('/')[-1].split('_')[0])
        dbxrefs[col_lab + 'LABEL'] = dbxrefs[col_lab + 'URI'].apply(lambda x: ont_labels[x])
        # update evidence formatting --> EX: CONCEPTS_DBXREF_UMLS:C0008533
        dbxrefs[col_lab + 'EVIDENCE'] = dbxrefs['CODE'].apply(lambda x: col_lab[0:-4] + x)
        # drop unneeded columns
        dbxrefs = dbxrefs[[primary_key] + [x for x in list(dbxrefs.columns) if x.startswith(col_lab[0:-4])]]

        return dbxrefs.drop_duplicates()

    def exact_string_mapper(self, data: pd.DataFrame, primary_key: str, code_type: str) -> pd.DataFrame:
        """Takes a stacked Pandas DataFrame and merges it with a Pandas DataFrame version of the ontology-dictionary
        object 'label' and 'synonym' data.

            INPUT:
                    CONCEPT_ID                         CONCEPT_LABEL                                 CONCEPT_SYNONYM
                0      4331309   Myocarditis due to infectious agent              Myocarditis due to infectious agent
                1      4331309   Myocarditis due to infectious agent                            Infective myocarditis
                2      4331309   Myocarditis due to infectious agent   Myocarditis due to infectious agent (disorder)

            OUTPUT:
                      CONCEPT_ID                  CODE     CODE_COLUMN   ONT_URI     ONT             EVIDENCE
                0        4141365  engraftment syndrome   CONCEPT_LABEL       URL   MONDO     LABEL_CONCEPT_ID
                1        4141365  engraftment syndrome  CONCEPT_SYNONYM      URL   MONDO     LABEL_CONCEPT_ID
                2         133835                eczema    CONCEPT_LABEL      URL      HP     LABEL_CONCEPT_ID
        Args:
            data: A stacked Pandas DataFrame containing output from the umls_cui_annotator method (see INPUT above
                for an example).
            primary_key: A string containing the name of the primary key (i.e. CONCEPT_ID).
            code_type: A string containing the concept_level (i.e. concept or ancestor).

        Returns:
            merged_strings: A Pandas DataFrame containing the results from string matching the ontology strings to
                the clinical strings (see OUTPUT above for an example).
        """

        col_label = code_type.upper() + '_STR_ONT_'  # column labels
        ont_labels = merge_dictionaries(self.ont_dict, 'label', reverse=True)
        data['CODE'] = data['CODE'].apply(lambda x: x.lower())  # prepare clinical data

        # prepare ontology data
        ont_dfs = []
        for str_col in ['label', 'synonym']:
            combo_dict_df_label = pd.concat([pd.DataFrame(self.ont_dict[ont][str_col].items(),
                                                          columns=['CODE', col_label + 'URI']) for ont in
                                             self.ont_dict.keys()])

            # merge ontology data and clinical data
            str_data = data.merge(combo_dict_df_label, how='inner', on='CODE').drop_duplicates()
            # update ontology data formatting
            str_data[col_label + 'TYPE'] = str_data[col_label + 'URI'].apply(lambda x: x.split('/')[-1].split('_')[0])
            str_data[col_label + 'LABEL'] = str_data[col_label + 'URI'].apply(lambda x: ont_labels[x])
            # update evidence formatting --> EX: CONCEPT_SYNONYM:dic_in_newborn
            aggregated_evidence = str_data['CODE'].apply(lambda x: x.replace(' ', '_'))
            str_data[col_label + 'EVIDENCE'] = str_data['CODE_COLUMN'] + ':' + aggregated_evidence
            # drop unneeded columns
            str_data = str_data[[primary_key] + [x for x in list(str_data.columns) if x.startswith(col_label[0:-4])]]
            ont_dfs.append(str_data.drop_duplicates())

        return pd.concat(ont_dfs).drop_duplicates()

    def clinical_concept_mapper(self) -> pd.DataFrame:
        """This method serves as the main method for this class. it's purpose is to iterate over all relevant data in
        an input clinical data file and generate several different kinds of mappings to a ontologies provided in an
        input dictionary. The script annotates the data on two levels: concepts and concept ancestors. For both
        levels, the following steps are completed to derive concept annotations:
            1 - UMLS CUIs and semantics types to concept ids
            2 - Ontology dbXRefs between concept ids and ontology ids
            3 - Exact string matching concept labels and synonyms to ontology labels and synonyms
            4 - Aggregating the results from steps 1-3 into a single Pandas DataFrame
            5 - Combine results from each level into single Pandas DataFrame

        Returns:
            complete_map: A Pandas DataFrame containing the results of performing dbXRef and exact string mapping to
                the input ontologies and clinical data.
        """

        level_maps = []

        if self.ancestor_codes is not None:
            levels = {'concept': {'codes': self.concept_codes, 'strings': self.concept_strings},
                      'ancestor': {'codes': self.ancestor_codes,
                                   'strings': self.ancestor_strings}}
        else:
            levels = {'concept': {'codes': self.concept_codes, 'strings': self.concept_strings}}

        for level in levels.keys():
            print('\n*** Annotating Level: {}'.format(level))
            primary_key, data = self.primary_key, self.clinical_data.copy()
            code_level, code_strings = levels[level]['codes'][0], levels[level]['strings']  # type: ignore
            if level == 'ancestor' or any(x for x in data[code_level] if '|' in x):
                data = column_splitter(data, primary_key, [code_level], '|')[[primary_key] + [code_level]]
                data[code_level] = normalizes_source_codes(data[code_level].to_frame(), self.source_code_map)
            else:
                data[code_level] = normalizes_source_codes(data[code_level].to_frame(), self.source_code_map)

            # STEP 1: UMLS CUI + SEMANTIC TYPE ANNOTATION
            print('Performing UMLS CUI + Semantic Type Annotation')
            if self.umls_cui_data is not None and self.umls_tui_data is not None:
                umls_map = self.umls_cui_annotator(data.copy(), primary_key, code_level)
                sub = [code_level, 'UMLS_CODE', 'UMLS_CUI']
                data_stacked = data_frame_subsetter(umls_map[[primary_key] + sub], primary_key, sub)
            else:
                print('Did not provide MRCONSO and MRSTY Files -- Skipping UMLS Annotation Step')
                umls_map, clinical_subset = None, data[[primary_key, code_level]]
                data_stacked = data_frame_subsetter(clinical_subset, primary_key, [code_level])

            # STEP 2 - DBXREF ANNOTATION
            print('Performing DbXRef Annotation')
            stacked_dbxref = self.dbxref_mapper(data_stacked.copy(), primary_key, level)
            # files = 'resources/mappings/' + level + '_dbXRef_Mappings.csv'
            # stacked_dbxref.to_csv(files, sep=',', index=False, header=True)

            # STEP 3 - EXACT STRING MAPPING
            print('Performing Exact String Mapping')
            clinical_strings = self.clinical_data.copy()[[primary_key] + code_strings]  # type: ignore
            split_strings = column_splitter(clinical_strings, primary_key, code_strings, '|')  # type: ignore
            split_strings = split_strings[[primary_key] + code_strings]  # type: ignore
            split_strings_stacked = data_frame_subsetter(split_strings, primary_key, code_strings)  # type: ignore
            stacked_strings = self.exact_string_mapper(split_strings_stacked, primary_key, level)
            # files_str = 'resources/mappings/' + level + '_String_Mappings.csv'
            # stacked_strings.to_csv(files_str, sep=',', index=False, header=True)

            # STEP 4 - COMBINE RESULTS
            print('Aggregating Mapping Results')
            # dbXRef annotations
            if len(stacked_dbxref) != 0:
                ont_type_column = [col for col in stacked_dbxref.columns if 'TYPE' in col][0]
                dbxrefs = data_frame_grouper(stacked_dbxref.copy(), primary_key, ont_type_column,
                                             aggregates_column_values)
            else:
                dbxrefs = None

            # exact string annotations
            if len(stacked_strings) != 0:
                ont_type_column = [col for col in stacked_strings.columns if 'TYPE' in col][0]
                strings = data_frame_grouper(stacked_strings.copy(), primary_key, ont_type_column,
                                             aggregates_column_values)
            else:
                strings = None

            # umls annotations
            if umls_map is not None:
                umls, agg_cols = umls_map[[primary_key, 'UMLS_CUI', 'UMLS_SEM_TYPE']], ['UMLS_CUI', 'UMLS_SEM_TYPE']
                umls = aggregates_column_values(umls.copy(), primary_key, agg_cols, ' | ')
                umls.columns = [primary_key] + [level.upper() + '_' + x for x in umls.columns if x != primary_key]
            else:
                umls = None

            # combine annotations
            dfs = [x for x in [dbxrefs, strings, umls] if x is not None]
            if len(dfs) > 1:
                level_maps.append(reduce(lambda x, y: pd.merge(x, y, how='outer', on=primary_key), dfs))
            else:
                level_maps.append(dfs[0])

        # STEP 5 - COMBINE CONCEPT AND ANCESTOR DATA
        print('Combining Concept and Ancestor Maps')
        full_map = reduce(lambda x, y: pd.merge(x, y, how='outer', on=self.primary_key), level_maps)
        complete_map = pd.merge(self.clinical_data, full_map, how='left', on=self.primary_key)
        complete_map.columns = [x.upper() for x in complete_map.columns]
        complete_map.fillna('', inplace=True)

        return complete_map
