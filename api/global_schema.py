def making_global_schema(*args):

    global_mapping = {

        'atc_classifications': ['atc_classifications', None, None],
        'availability_type': ['availability_type', None, None],
        'biotherapeutic': ['biotherapeutic', None, None],
        'black_box_warning': ['black_box_warning', None, None],
        'chebi_par_id': ['chebi_par_id', None, None],
        'chemical_probe': ['chemical_probe', None, None],
        'chirality': ['chirality', None, None],
        'cross_references': ['cross_references', None, None],
        'dosed_ingredient': ['dosed_ingredient', None, None],
        'first_approval': ['first_approval', None, None],
        'first_in_class': ['first_in_class', None, None],
        'helm_notation': ['helm_notation', None, None],
        'indication_class': ['indication_class', None, None],
        'inorganic_flag': ['inorganic_flag', None, None],
        'max_phase': ['max_phase', None, None],
        'molecule_chembl_id': ['molecule_chembl_id', None, None],
        'molecule_hierarchy': ['molecule_hierarchy', None, None],
        # 'molecule_properties': ['molecule_properties', None, None],
        # 'molecule_structures': ['molecule_structures', None, None],
        'molecule_synonyms': ['molecule_synonyms', None, None],
        'molecule_type': ['molecule_type', None, None],
        'natural_product': ['natural_product', None, None],
        'oral': ['oral', None, None],
        'parenteral': ['parenteral', None, None],
        'polymer_flag': ['polymer_flag', None, None],
        'prodrug': ['prodrug', None, None],
        'structure_type': ['structure_type', None, None],
        'therapeutic_flag': ['therapeutic_flag', None, None],
        'topical': ['topical', None, None],
        'usan_stem': ['usan_stem', None, None],
        'usan_stem_definition': ['usan_stem_definition', None, None],
        'usan_substem': ['usan_substem', None, None],
        'usan_year': ['usan_year', None, None],
        'withdrawn_flag': ['withdrawn_flag', None, None],
        

        #MOLECULAR PROPERTIES
        'alogp': ['alogp', None, None],
        'aromatic_rings': ['aromatic_rings', None, None],
        'cx_logd': ['cx_logd', None, None],
        'cx_logp': ['cx_logp', None, None],
        'cx_most_apka': ['cx_most_apka', None, None],
        'cx_most_bpka': ['cx_most_bpka', None, None],
        'full_molformula': ['full_molformula', 'formula', None],
        'full_mwt': ['full_mwt', 'molecular_weight', None],
        # 'hba': ['hba', 'h_bond_acceptor_count', None],
        'hba_lipinski': ['hba_lipinski', None, None],
        # 'hbd': ['hbd', 'h_bond_donor_count', None],
        'hbd_lipinski': ['hbd_lipinski', None, None],
        'heavy_atoms': ['heavy_atoms', 'heavy_atom_count', None],
        'molecular_species': ['molecular_species', None, None],
        'mw_freebase': ['mw_freebase', None, None],
        'mw_monoisotopic': ['mw_monoisotopic', 'monoisotopic_mass', None],
        'np_likeness_score': ['np_likeness_score', None, None],
        'num_lipinski_ro5_violations': ['num_lipinski_ro5_violations', None, None],
        'num_ro5_violations': ['num_ro5_violations', None, None],
        'psa': ['psa', None, None],
        'qed_weighted': ['qed_weighted', None, None],
        'ro3_pass': ['ro3_pass', None, None],
        'rtb': ['rtb', None, None],


        #MOLECULAR STRUCTURE
        'canonical_smiles': ['canonical_smiles', 'canonical_smiles', None],
        'isomeric_smiles': [None, 'isomeric_smiles', None],
        'molfile': ['molfile', None, None],
        'standard_inchi': ['standard_inchi', 'inchi', None],
        'standard_inchi_key': ['standard_inchi_key', 'inchikey', None],



        'atom_stereo_count': [None, 'atom_stereo_count', None],
        'bond_stereo_count': [None, 'bond_stereo_count', None],
        'cactvs_fingerprint': [None, 'cactvs_fingerprint', None],
        # 'canonical_smiles': [None, 'canonical_smiles', None],
        'charge': [None, 'charge', None],
        'cid': [None, 'cid', None],
        'complexity': [None, 'complexity', None],
        'conformer_id_3d': [None, 'conformer_id_3d', None],
        'conformer_rmsd_3d': [None, 'conformer_rmsd_3d', None],
        'coordinate_type': [None, 'coordinate_type', None],
        'covalent_unit_count': [None, 'covalent_unit_count', None],
        'defined_atom_stereo_count': [None, 'defined_atom_stereo_count', None],
        'defined_bond_stereo_count': [None, 'defined_bond_stereo_count', None],
        'effective_rotor_count_3d': [None, 'effective_rotor_count_3d', None],
        'elements': [None, 'elements', None],
        'exact_mass': [None, 'exact_mass', None],
        'feature_selfoverlap_3d': [None, 'feature_selfoverlap_3d', None],
        'fingerprint': [None, 'fingerprint', None],
        'h_bond_acceptor_count': [None, 'h_bond_acceptor_count', None],
        'h_bond_donor_count': [None, 'h_bond_donor_count', None],
        'heavy_atom_count': [None, 'heavy_atom_count', None],
        # 'inchi': [None, 'inchi', None],
        # 'inchikey': [None, 'inchikey', None],
        # 'isomeric_smiles': [None, 'isomeric_smiles', None],
        'isotope_atom_count': [None, 'isotope_atom_count', None],
        'iupac_name': [None, 'iupac_name', None],
        'mmff94_energy_3d': [None, 'mmff94_energy_3d', None],
        'mmff94_partial_charges_3d': [None, 'mmff94_partial_charges_3d', None],
        # 'molecular_formula': [None, 'molecular_formula', None],
        # 'molecular_weight': [None, 'molecular_weight', None],
        'monoisotopic_mass': [None, 'monoisotopic_mass', None],
        'multipoles_3d': [None, 'multipoles_3d', None],
        'pharmacophore_features_3d': [None, 'pharmacophore_features_3d', None],
        'rotatable_bond_count': [None, 'rotatable_bond_count', None],
        'shape_fingerprint_3d': [None, 'shape_fingerprint_3d', None],
        'shape_selfoverlap_3d': [None, 'shape_selfoverlap_3d', None],
        'tpsa': [None, 'tpsa', None],
        'undefined_atom_stereo_count': [None, 'undefined_atom_stereo_count', None],
        'undefined_bond_stereo_count': [None, 'undefined_bond_stereo_count', None],
        'volume_3d': [None, 'volume_3d', None],
        'xlogp': [None, 'xlogp', None],

    }


    global_mapping_2 = {

        'atc_classifications': ['atc_classifications', None, None],
        'availability_type': ['availability_type', None, None],
        'biotherapeutic': ['biotherapeutic', None, None],
        'black_box_warning': ['black_box_warning', None, None],
        'chebi_par_id': ['chebi_par_id', None, None],
        'chemical_probe': ['chemical_probe', None, None],
        'chirality': ['chirality', None, None],
        'cross_references': ['cross_references', None, None],
        'dosed_ingredient': ['dosed_ingredient', None, None],
        'first_approval': ['first_approval', None, None],
        'first_in_class': ['first_in_class', None, None],
        'helm_notation': ['helm_notation', None, None],
        'indication_class': ['indication_class', None, None],
        'inorganic_flag': ['inorganic_flag', None, None],
        'max_phase': ['max_phase', None, None],
        'molecule_chembl_id': ['molecule_chembl_id', None, None],
        'molecule_hierarchy': ['molecule_hierarchy', None, None],
        # 'molecule_properties': ['molecule_properties', None, None],
        # 'molecule_structures': ['molecule_structures', None, None],
        'molecule_synonyms': ['molecule_synonyms', None, None],
        'molecule_type': ['molecule_type', None, None],
        'natural_product': ['natural_product', None, None],
        'oral': ['oral', None, None],
        'parenteral': ['parenteral', None, None],
        'polymer_flag': ['polymer_flag', None, None],
        'prodrug': ['prodrug', None, None],
        'structure_type': ['structure_type', None, None],
        'therapeutic_flag': ['therapeutic_flag', None, None],
        'topical': ['topical', None, None],
        'usan_stem': ['usan_stem', None, None],
        'usan_stem_definition': ['usan_stem_definition', None, None],
        'usan_substem': ['usan_substem', None, None],
        'usan_year': ['usan_year', None, None],
        'withdrawn_flag': ['withdrawn_flag', None, None],
        

        #MOLECULAR PROPERTIES
        # 'syn_type': ['syn_type', None, None],
        'alogp': ['alogp', None, None],
        'aromatic_rings': ['aromatic_rings', None, None],
        'cx_logd': ['cx_logd', None, None],
        'cx_logp': ['cx_logp', None, None],
        'cx_most_apka': ['cx_most_apka', None, None],
        'cx_most_bpka': ['cx_most_bpka', None, None],
        'full_molformula': ['full_molformula', 'formula', None],
        'full_mwt': ['full_mwt', 'molecular_weight', None],
        # 'hba': ['hba', 'h_bond_acceptor_count', None],
        'hba_lipinski': ['hba_lipinski', None, None],
        # 'hbd': ['hbd', 'h_bond_donor_count', None],
        'hbd_lipinski': ['hbd_lipinski', None, None],
        'heavy_atoms': ['heavy_atoms', 'heavy_atom_count', None],
        'molecular_species': ['molecular_species', None, None],
        'mw_freebase': ['mw_freebase', None, None],
        'mw_monoisotopic': ['mw_monoisotopic', 'monoisotopic_mass', None],
        'np_likeness_score': ['np_likeness_score', None, None],
        'num_lipinski_ro5_violations': ['num_lipinski_ro5_violations', None, None],
        'num_ro5_violations': ['num_ro5_violations', None, None],
        'psa': ['psa', None, None],
        'qed_weighted': ['qed_weighted', None, None],
        'ro3_pass': ['ro3_pass', None, None],
        'rtb': ['rtb', None, None],


        #MOLECULAR STRUCTURE
        'canonical_smiles': ['canonical_smiles', 'canonical_smiles', None],
        'isomeric_smiles': [None, 'isomeric_smiles', None],
        'molfile': ['molfile', None, None],
        'standard_inchi': ['standard_inchi', 'inchi', None],
        'standard_inchi_key': ['standard_inchi_key', 'inchikey', None],



        'atom_stereo_count': [None, 'atom_stereo_count', None],
        'bond_stereo_count': [None, 'bond_stereo_count', None],
        'cactvs_fingerprint': [None, 'cactvs_fingerprint', None],
        # 'canonical_smiles': [None, 'canonical_smiles', None],
        'charge': [None, 'charge', None],
        'cid': [None, 'cid', None],
        'complexity': [None, 'complexity', None],
        'conformer_id_3d': [None, 'conformer_id_3d', None],
        'conformer_rmsd_3d': [None, 'conformer_rmsd_3d', None],
        'coordinate_type': [None, 'coordinate_type', None],
        'covalent_unit_count': [None, 'covalent_unit_count', None],
        'defined_atom_stereo_count': [None, 'defined_atom_stereo_count', None],
        'defined_bond_stereo_count': [None, 'defined_bond_stereo_count', None],
        'effective_rotor_count_3d': [None, 'effective_rotor_count_3d', None],
        'elements': [None, 'elements', None],
        'exact_mass': [None, 'exact_mass', None],
        'feature_selfoverlap_3d': [None, 'feature_selfoverlap_3d', None],
        'fingerprint': [None, 'fingerprint', None],
        'h_bond_acceptor_count': [None, 'h_bond_acceptor_count', None],
        'h_bond_donor_count': [None, 'h_bond_donor_count', None],
        'heavy_atom_count': [None, 'heavy_atom_count', None],
        # 'inchi': [None, 'inchi', None],
        # 'inchikey': [None, 'inchikey', None],
        # 'isomeric_smiles': [None, 'isomeric_smiles', None],
        'isotope_atom_count': [None, 'isotope_atom_count', None],
        'iupac_name': [None, 'iupac_name', None],
        'mmff94_energy_3d': [None, 'mmff94_energy_3d', None],
        'mmff94_partial_charges_3d': [None, 'mmff94_partial_charges_3d', None],
        # 'molecular_formula': [None, 'molecular_formula', None],
        # 'molecular_weight': [None, 'molecular_weight', None],
        'monoisotopic_mass': [None, 'monoisotopic_mass', None],
        'multipoles_3d': [None, 'multipoles_3d', None],
        'pharmacophore_features_3d': [None, 'pharmacophore_features_3d', None],
        'rotatable_bond_count': [None, 'rotatable_bond_count', None],
        'shape_fingerprint_3d': [None, 'shape_fingerprint_3d', None],
        'shape_selfoverlap_3d': [None, 'shape_selfoverlap_3d', None],
        'tpsa': [None, 'tpsa', None],
        'undefined_atom_stereo_count': [None, 'undefined_atom_stereo_count', None],
        'undefined_bond_stereo_count': [None, 'undefined_bond_stereo_count', None],
        'volume_3d': [None, 'volume_3d', None],
        'xlogp': [None, 'xlogp', None],

        # ['compounds', 'notFound', 'response', 'totalCompounds']) 
        'compounds':[None, None , 'compounds'],
        'notFound':[None, None , 'notFound'],
        'response':[None, None , 'response'],
        'totalCompounds':[None, None , 'totalCompounds'],


    }


    global_attributes = list(global_mapping.keys())
    global_values = {key: 0 for key in global_attributes}

    global_attributes_2 = list(global_mapping_2.keys())
    global_values_2 = {key: 0 for key in global_attributes_2}

    print(len(global_attributes_2))
    combined_dict = {}
    combined_dict = {key: value for dictionary in args for key, value in dictionary.items()}

    print(combined_dict.keys())
    print(len(combined_dict.keys()))

    
    try:
        for mapping, (chembl_key, pubchem_key , unichem_key) in global_mapping_2.items():
            if chembl_key is not None:
                global_values_2[mapping] = combined_dict[chembl_key]   
            elif chembl_key is None and pubchem_key is not None:
                global_values_2[mapping] = combined_dict[pubchem_key]
            elif pubchem_key is None and chembl_key is None:
                global_values_2[mapping] = combined_dict[unichem_key]
            else:
                continue
        return global_values_2
        
    except:
        for mapping, (chembl_key, pubchem_key , unichem_key) in global_mapping.items():
            if chembl_key is not None:
                global_values[mapping] = combined_dict[chembl_key]   
            elif chembl_key is None and pubchem_key is not None:
                global_values[mapping] = combined_dict[pubchem_key]
            elif pubchem_key is None and chembl_key is None:
                global_values[mapping] = combined_dict[unichem_key]
            else:
                continue
        return global_values

    

# def schema_mapping(global_mapping , chembl_data , pubchem_data)
    ##Algorithm For Entity mapping
    # for mapping, (chembl_key, pubchem_key , drugbank_key) in global_mapping.items():
    #         if chembl_key is None:
    #             global_values[mapping] = pubchem_values[pubchem_key]
    #         elif pubchem_key is None:
    #             global_values[mapping] = chembl_values[chembl_key]
    #         elif chembl_key is None and pubchem_key is None:
    #             global_values[mapping] = drugbank_values[drugbank_key]
    #         else:
    #             global_values[mapping] = chembl_values[chembl_key]

