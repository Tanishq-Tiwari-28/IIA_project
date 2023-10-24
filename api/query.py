import pubchempy as pcp
import json
def is_serializable(data):
    try:
        json.dumps(data)
        return True  # The dictionary is serializable
    except TypeError:
        return False  # The dictionary is not serializable



def get_drug_info_pubchem(name):
    print("in pubchem")
    try:
        compounds = pcp.get_compounds(name, 'name')
        if not compounds:
            print(f"No compound found for '{name}'")
            return
        drug_info_list = []
        for compound in compounds:
            compound_dict = compound.to_dict()
            drug_info_list.append(compound_dict)
        # print(drug_info_list)

        pubchem_attributes = []
        if drug_info_list:
            first_dict = drug_info_list[0]
            pubchem_attributes = list(first_dict.keys())

        print((pubchem_attributes))
        print(len(pubchem_attributes))

        pubchem_values = {attr: 0 for attr in pubchem_attributes}

        for attr in pubchem_attributes:
            for info_dict in drug_info_list:
                if attr in info_dict:
                    pubchem_values[attr] = info_dict[attr]
                    break
          
        # print((pubchem_values))

        print(is_serializable(pubchem_values))
        return pubchem_values
    except Exception as e:
        print("Error:", str(e))



def get_drug_info_chembl(name):
    print('in names_chembl')
    try:
        from chembl_webresource_client.new_client import new_client
        drug_name = name
        molecule = new_client.molecule
        mols = molecule.filter(molecule_synonyms__molecule_synonym__iexact=drug_name).only('molecule_chembl_id')
        for mol in mols:
            print(f"ChEMBL ID for {drug_name}: {mol['molecule_chembl_id']}")
        chembl_id = mol['molecule_chembl_id']
        drug_info = molecule.get(chembl_id)
        print("Drug Information for ChEMBL ID:", chembl_id)
        # print(drug_info)
        # molecule_properties = drug_info.get('molecule_properties')
        # molecule_structures = drug_info.get('molecule_structures')
        # molecule_synonym = drug_info.get('molecule_synonyms')

        # chembl_attributes= []
        # if drug_info:
        #     first_dict = drug_info[0]
        #     chembl_attributes = list(first_dict.keys())

        # print((chembl_attributes))
        # print(len(chembl_attributes))

        # chembl_values = {attr: 0 for attr in chembl_attributes}

        # for attr in chembl_attributes:
        #     if attr in drug_info:
        #         chembl_values[attr] = drug_info[attr]
        # for attr in chembl_attributes:
        #     if attr in molecule_properties:
        #         chembl_values[attr] = molecule_properties[attr]
        # for attr in chembl_attributes:
        #     if attr in molecule_structures:
        #         chembl_values[attr] = molecule_structures[attr]
        print(len(drug_info))
        print(is_serializable(drug_info))

        # print((drug_info))

        return drug_info
    except Exception as e:
        return "Error: " + str(e)


def get_drug_from_Unichem(inchi_key):
    # UNICHEM API URL
    import requests , json
    url = "https://www.ebi.ac.uk/unichem/api/v1/compounds"
    payload = {
        "type": 'inchikey',
        "compound": inchi_key
    }
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", url, json=payload, headers=headers)
    print(type(response.text))

    data_dict = json.loads(response.text)
    print(type(data_dict))

# get_drug_from_Unichem("BNRNXUUZRGQAQC-UHFFFAOYSA-N")


# chembl_attributes = [
#     "chembl_id",
#     "pref_name",
#     'atc_classifications',
#     "availability_type",
#     "biotherapeutic",
#     "black_box_warning",
#     "chebi_par_id",
#     "chemical_probe",
#     "chirality",
#     "cross_references",
#     "dosed_ingredient",
#     "first_approval",
#     "first_in_class",
#     "helm_notation",
#     "indication_class",
#     "inorganic_flag",
#     "max_phase",
#     "molecule_chembl_id",
#     "molecule_hierarchy",
#     "molecule_type",
#     "natural_product",
#     "oral",
#     "parenteral",
#     "polymer_flag",
#     "prodrug",
#     "structure_type",
#     "therapeutic_flag",
#     "topical",
#     "usan_stem",
#     "usan_stem_definition",
#     "usan_substem",
#     "usan_year",
#     "withdrawn_flag",

#     "molecule_synonym",
#     "syn_type",

#     "alogp",
#     "aromatic_rings",
#     "cx_logd",
#     "cx_logp",
#     "cx_most_pka1",
#     "cx_most_pka2",
#     "full_molformula",
#     "full_mwt",
#     "hba",
#     "hba_lipinski",
#     "hbd",
#     "hbd_lipinski",
#     "heavy_atoms",
#     "molecular_species",
#     "mw_freebase",
#     "mw_monoisotopic",
#     "np_likeness_score",
#     "num_lipinski_ro5_violations",
#     "num_ro5_violations",
#     "psa",
#     "qed_weighted",
#     "ro3_pass",
#     "rtb",

#     "canonical_smiles",
#     "molfile",
#     "standard_inchi",
#     "standard_inchi_key",


#     # "xref_name"
#     # "xref_src"
# ]

# print(len(chembl_attributes))
# chembl_values = {attr: 0 for attr in chembl_attributes}


# pubchem_attributes = [
#     "cactvs_fingerprint",
#     "canonical_smiles",
#     "charge",
#     "cid",
#     "complexity",
#     "conformer_id_3d",
#     "conformer_rmsd_3d",
#     "coordinate_type",
#     "covalent_unit_count",
#     "defined_atom_stereo_count",
#     "defined_bond_stereo_count",
#     "effective_rotor_count_3d",
#     "exact_mass",
#     "feature_selfoverlap_3d",
#     "fingerprint",
#     "h_bond_acceptor_count",
#     "h_bond_donor_count",
#     "inchi",
#     "inchikey",
#     "isomeric_smiles",
#     "isotope_atom_count",
#     "iupac_name",
#     "mmff94_energy_3d",
#     "mmff94_partial_charges_3d",
#     "molecular_formula",
#     "molecular_weight",
#     "monoisotopic_mass",
#     "multipoles_3d",
#     "pharmacophore_features_3d",
#     'charge',
#     "rotatable_bond_count",
#     "shape_fingerprint_3d",
#     "shape_selfoverlap_3d",
#     "tpsa",
#     "undefined_atom_stereo_count",
#     "undefined_bond_stereo_count",
#     "volume_3d",
#     "xlogp"
# ]


# print(len(pubchem_attributes))
# pubchem_values = {attr: 0 for attr in pubchem_attributes}

# drugbank_attributes = [
#     "compound",
#     "description",
#     "state",
#     "indication",
#     "pharmacodynamics",
#     "mechanism_of_action",
#     "toxicity",
#     "metabolism",
#     "absorption",
#     "half_life",
#     "protein_binding",
#     "route_of_elimination",
#     "volume_of_distribution",
#     "clearance"
# ]
# drugbank_values = {attr: 0 for attr in drugbank_attributes}


# List of attributes from the global schema
# def making_global_schema(chembl_data , pubchem_data):
#     global_schema = {}
    # Update the global schema with the keys and values from the first dictionary
    # global_schema.update(chembl_data)

    # Update the global schema with the keys and values from the second dictionary
    # global_schema.update(pubchem_data)
    # print(len(global_schema))
    # print(global_schema)
    


# global_attributes = [
#     "drug_id", "name", "atc_classifications", "availability_type",
#     "biotherapeutic", "black_box_warning", "chebi_par_id", "chemical_probe",
#     "chirality", "cross_references", "dosed_ingredient", "first_approval",
#     "first_in_class", "helm_notation", "indication_class", "inorganic_flag",
#     "max_phase", "molecule_chembl_id", "molecule_hierarchy", "molecule_type",
#     "natural_product", "oral", "parenteral", "polymer_flag", "prodrug",
#     "structure_type", "therapeutic_flag", "topical", "usan_stem",
#     "usan_stem_definition", "usan_substem", "usan_year", "withdrawn_flag",
#     "molecule_synonym", "syn_type",  "alogp", "aromatic_rings",
#     "cx_logd", "cx_logp", "cx_most_pka1", "cx_most_pka2", "full_molformula", "full_mwt",
#     "hba", "hba_lipinski", "hbd", "hbd_lipinski", "heavy_atoms",
#     "molecular_species", "mw_freebase", "mw_monoisotopic", "np_likeness_score",
#     "num_lipinski_ro5_violations", "num_ro5_violations", "psa", "qed_weighted",
#     "ro3_pass", "rtb", "rotatable_bond_count", "fingerprint", "fingerprint_type",
#     "canonical_smiles", "isomeric_smiles", "molfile", "standard_inchi", "standard_inchi_key",
#     "cactvs_fingerprint", "cid", "complexity", "conformer_id_3d", "conformer_rmsd_3d", "coordinate_type", "covalent_unit_count", "defined_atom_stereo_count", "defined_bond_stereo_count", "effective_rotor_count_3d", "feature_selfoverlap_3d", "fingerprint", "isotope_atom_count", "iupac_name", "mmff94_energy_3d", "mmff94_partial_charges_3d", "multipoles_3d", "pharmacophore_features_3d", 'charge', "rotatable_bond_count", "shape_fingerprint_3d", "shape_selfoverlap_3d", "tpsa", "undefined_atom_stereo_count", "undefined_bond_stereo_count", "volume_3d", "xlogp" , "compound","description","state","indication","pharmacodynamics","mechanism_of_action","toxicity","metabolism","absorption","half_life" "protein_binding","route_of_elimination","volume_of_distribution","clearance"
# ]

# print(len(global_attributes))


# global_mapping = {}

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




# Mapping between ChEMBL schema and Pubchem schema to Global schema
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

    # 'compound': [None, None, 'compound'],   
    # 'description': [None, None, 'description'],
    # 'state': [None, None, 'state'],
    # 'indication': [None, None, 'indication'],
    # 'pharmacodynamics': [None, None, 'pharmacodynamics'],
    # 'mechanism_of_action': [None, None, 'mechanism_of_action'],
    # 'toxicity': [None, None, 'toxicity'],
    # 'metabolism': [None, None, 'metabolism'],
    # 'absorption': [None, None, 'absorption'],
    # 'half_life': [None, None, 'half_life'],
    # 'protein_binding': [None, None, 'protein_binding'],
    # 'route_of_elimination': [None, None, 'route_of_elimination'],
    # 'volume_of_distribution': [None, None, 'volume_of_distribution'],
    # 'clearance': [None, None, 'clearance']
    
# } 




# def tranform(chembl_values , pubchem_values , gloabl_values, global_mapping ):



