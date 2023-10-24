def making_global_schema(chembl_data , pubchem_data):
    global_schema = {}
    # Update the global schema with the keys and values from the first dictionary
    global_schema.update(chembl_data)

    # Update the global schema with the keys and values from the second dictionary
    global_schema.update(pubchem_data)
    print(len(global_schema))


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




import difflib
def schema_mapping(chembl_data , pubchem_data):
    mapping_chembl_pubchem = {}
    for key_chembl in chembl_data:
        for key_pubchem in pubchem_data:
            similarity = difflib.SequenceMatcher(None, key_chembl, key_pubchem).ratio()

            # Define a similarity threshold (adjust as needed)
            if similarity > 0.6:
                mapping_chembl_pubchem[key_chembl] = key_pubchem


    # Create the global mapping dictionary
    global_mapping = {}
    for key_global in set(chembl_data.keys()) | set(pubchem_data.keys()):
        global_mapping[key_global] = [mapping_chembl_pubchem.get(key_global), key_global]


    # Print the global mapping dictionary
    print("Global Mapping Dictionary:")
    for key, value in global_mapping.items():
        print(f"{key} maps to Chembl attribute: {value[0]}, PubChem attribute: {value[1]}")




# global_mapping = {
#     'drug_id': ['chembl_id', 'compound_id', None],
#     'name': ['pref_name', 'name', None],
#     'atc_classifications': ['atc_classifications', None, None],
#     'availability_type': ['availability_type', None, None],
#     'biotherapeutic': ['biotherapeutic', None, None],
#     'black_box_warning': ['black_box_warning', None, None],
#     'chebi_par_id': ['chebi_par_id', None, None],
#     'chemical_probe': ['chemical_probe', None, None],
#     'chirality': ['chirality', None, None],
#     'cross_references': ['cross_references', None, None],
#     'dosed_ingredient': ['dosed_ingredient', None, None],
#     'first_approval': ['first_approval', None, None],
#     'first_in_class': ['first_in_class', None, None],
#     'helm_notation': ['helm_notation', None, None],
#     'indication_class': ['indication_class', None, None],
#     'inorganic_flag': ['inorganic_flag', None, None],
#     'max_phase': ['max_phase', None, None],
#     'molecule_chembl_id': ['molecule_chembl_id', None, None],
#     'molecule_hierarchy': ['molecule_hierarchy', None, None],
#     'molecule_type': ['molecule_type', None, None],
#     'natural_product': ['natural_product', None, None],
#     'oral': ['oral', None, None],
#     'parenteral': ['parenteral', None, None],
#     'polymer_flag': ['polymer_flag', None, None],
#     'prodrug': ['prodrug', None, None],
#     'structure_type': ['structure_type', None, None],
#     'therapeutic_flag': ['therapeutic_flag', None, None],
#     'topical': ['topical', None, None],
#     'usan_stem': ['usan_stem', None, None],
#     'usan_stem_definition': ['usan_stem_definition', None, None],
#     'usan_substem': ['usan_substem', None, None],
#     'usan_year': ['usan_year', None, None],
#     'withdrawn_flag': ['withdrawn_flag', None, None],
#     'molecule_synonym': ['molecule_synonym', None, None],
#     'syn_type': ['syn_type', None, None],
#     'alogp': ['alogp', None, None],
#     'aromatic_rings': ['aromatic_rings', None, None],
#     'cx_logd': ['cx_logd', None, None],
#     'cx_logp': ['cx_logp', None, None],
#     'cx_most_pka1': ['cx_most_pka1', None, None],
#     'cx_most_pka2': ['cx_most_pka2', None, None],
#     'full_molformula': ['full_molformula', 'formula', None],
#     'full_mwt': ['full_mwt', 'molecular_weight', None],
#     'hba': ['hba', 'h_bond_acceptor_count', None],
#     'hba_lipinski': ['hba_lipinski', None, None],
#     'hbd': ['hbd', 'h_bond_donor_count', None],
#     'hbd_lipinski': ['hbd_lipinski', None, None],
#     'heavy_atoms': ['heavy_atoms', 'heavy_atom_count', None],
#     'molecular_species': ['molecular_species', None, None],
#     'mw_freebase': ['mw_freebase', None, None],
#     'mw_monoisotopic': ['mw_monoisotopic', None, None],
#     'np_likeness_score': ['np_likeness_score', None, None],
#     'num_lipinski_ro5_violations': ['num_lipinski_ro5_violations', None, None],
#     'num_ro5_violations': ['num_ro5_violations', None, None],
#     'psa': ['psa', None, None],
#     'qed_weighted': ['qed_weighted', None, None],
#     'ro3_pass': ['ro3_pass', None, None],
#     'rtb': ['rtb', None, None],
#     'canonical_smiles': ['canonical_smiles', 'canonical_smiles', None],
#     'isomeric_smiles': [None, 'isomeric_smiles', None],
#     'molfile': ['molfile', None, None],
#     'standard_inchi': ['standard_inchi', 'inchi', None],
#     'standard_inchi_key': ['standard_inchi_key', 'inchikey', None],
#     'cactvs_fingerprint': [None, 'cactvs_fingerprint', None],
#     'cid': [None, 'cid', None],
#     'complexity': [None, 'complexity', None],
#     'conformer_id_3d': [None, 'conformer_id_3d', None],
#     'conformer_rmsd_3d': [None, 'conformer_rmsd_3d', None],
#     'coordinate_type': [None, 'coordinate_type', None],
#     'covalent_unit_count': [None, 'covalent_unit_count', None],
#     'defined_atom_stereo_count': [None, 'defined_atom_stereo_count', None],
#     'defined_bond_stereo_count': [None, 'defined_bond_stereo_count', None],
#     'effective_rotor_count_3d': [None, 'effective_rotor_count_3d', None],
#     'feature_selfoverlap_3d': [None, 'feature_selfoverlap_3d', None],
#     'fingerprint': [None, 'fingerprint', None],
#     'isotope_atom_count': [None, 'isotope_atom_count', None],
#     'iupac_name': [None, 'iupac_name', None],
#     'mmff94_energy_3d': [None, 'mmff94_energy_3d', None],
#     'mmff94_partial_charges_3d': [None, 'mmff94_partial_charges_3d', None],
#     'multipoles_3d': [None, 'multipoles_3d', None],
#     'pharmacophore_features_3d': [None, 'pharmacophore_features_3d', None],
#     'charge': [None, 'charge', None],
#     'rotatable_bond_count': [None, 'rotatable_bond_count', None],
#     'shape_fingerprint_3d': [None, 'shape_fingerprint_3d', None],
#     'shape_selfoverlap_3d': [None, 'shape_selfoverlap_3d', None],
#     'tpsa': [None, 'tpsa', None],
#     'undefined_atom_stereo_count': [None, 'undefined_atom_stereo_count', None],
#     'undefined_bond_stereo_count': [None, 'undefined_bond_stereo_count', None],
#     'volume_3d': [None, 'volume_3d', None],
#     'xlogp': [None, 'xlogp', None],
# }
