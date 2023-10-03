import pubchempy as pcp

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
        for attr in pubchem_attributes:
            for info_dict in drug_info_list:
                if attr in info_dict:
                    pubchem_values[attr] = info_dict[attr]
                    break  
        # print('pubchem' , pubchem_values)
        return drug_info_list
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
        molecule_properties = drug_info.get('molecule_properties')
        molecule_structures = drug_info.get('molecule_structures')
        molecule_synonym = drug_info.get('molecule_synonyms')

        for attr in chembl_attributes:
            if attr in drug_info:
                chembl_values[attr] = drug_info[attr]
        for attr in chembl_attributes:
            if attr in molecule_properties:
                chembl_values[attr] = molecule_properties[attr]
        for attr in chembl_attributes:
            if attr in molecule_structures:
                chembl_values[attr] = molecule_structures[attr]


        for mapping, (chembl_key, pubchem_key) in global_mapping.items():
            if chembl_key is None:
                global_values[mapping] = pubchem_values[pubchem_key]
            elif pubchem_key is None:
                global_values[mapping] = chembl_values[chembl_key]
            else:
                global_values[mapping] = chembl_values[chembl_key]
        print("global values" , global_values)
        return drug_info , global_values
    except Exception as e:
        return "Error: " + str(e)

 

chembl_attributes = [
    "chembl_id",
    "pref_name",
    'atc_classifications',
    "availability_type",
    "biotherapeutic",
    "black_box_warning",
    "chebi_par_id",
    "chemical_probe",
    "chirality",
    "cross_references",
    "dosed_ingredient",
    "first_approval",
    "first_in_class",
    "helm_notation",
    "indication_class",
    "inorganic_flag",
    "max_phase",
    "molecule_chembl_id",
    "molecule_hierarchy",
    "molecule_type",
    "natural_product",
    "oral",
    "parenteral",
    "polymer_flag",
    "prodrug",
    "structure_type",
    "therapeutic_flag",
    "topical",
    "usan_stem",
    "usan_stem_definition",
    "usan_substem",
    "usan_year",
    "withdrawn_flag",

    "molecule_synonym",
    "syn_type",

    "alogp",
    "aromatic_rings",
    "cx_logd",
    "cx_logp",
    "cx_most_pka1",
    "cx_most_pka2",
    "full_molformula",
    "full_mwt",
    "hba",
    "hba_lipinski",
    "hbd",
    "hbd_lipinski",
    "heavy_atoms",
    "molecular_species",
    "mw_freebase",
    "mw_monoisotopic",
    "np_likeness_score",
    "num_lipinski_ro5_violations",
    "num_ro5_violations",
    "psa",
    "qed_weighted",
    "ro3_pass",
    "rtb",

    "canonical_smiles",
    "molfile",
    "standard_inchi",
    "standard_inchi_key",


    # "xref_name"
    # "xref_src"
]

chembl_values = {attr: 0 for attr in chembl_attributes}


pubchem_attributes = [
    "cactvs_fingerprint",
    "canonical_smiles",
    "charge",
    "cid",
    "complexity",
    "conformer_id_3d",
    "conformer_rmsd_3d",
    "coordinate_type",
    "covalent_unit_count",
    "defined_atom_stereo_count",
    "defined_bond_stereo_count",
    "effective_rotor_count_3d",
    "exact_mass",
    "feature_selfoverlap_3d",
    "fingerprint",
    "h_bond_acceptor_count",
    "h_bond_donor_count",
    "inchi",
    "inchikey",
    "isomeric_smiles",
    "isotope_atom_count",
    "iupac_name",
    "mmff94_energy_3d",
    "mmff94_partial_charges_3d",
    "molecular_formula",
    "molecular_weight",
    "monoisotopic_mass",
    "multipoles_3d",
    "pharmacophore_features_3d",
    'charge',
    "rotatable_bond_count",
    "shape_fingerprint_3d",
    "shape_selfoverlap_3d",
    "tpsa",
    "undefined_atom_stereo_count",
    "undefined_bond_stereo_count",
    "volume_3d",
    "xlogp"
]

pubchem_values = {attr: 0 for attr in pubchem_attributes}



drugbank_attributes = [
    "compound",
    "description",
    "state",
    "indication",
    "pharmacodynamics",
    "mechanism_of_action",
    "toxicity",
    "metabolism",
    "absorption",
    "half_life",
    "protein_binding",
    "route_of_elimination",
    "volume_of_distribution",
    "clearance"
]
drugbank_values = {attr: 0 for attr in drugbank_attributes}

# List of attributes from the global schema
global_attributes = [
    "drug_id", "name", "atc_classifications", "availability_type",
    "biotherapeutic", "black_box_warning", "chebi_par_id", "chemical_probe",
    "chirality", "cross_references", "dosed_ingredient", "first_approval",
    "first_in_class", "helm_notation", "indication_class", "inorganic_flag",
    "max_phase", "molecule_chembl_id", "molecule_hierarchy", "molecule_type",
    "natural_product", "oral", "parenteral", "polymer_flag", "prodrug",
    "structure_type", "therapeutic_flag", "topical", "usan_stem",
    "usan_stem_definition", "usan_substem", "usan_year", "withdrawn_flag",
    "molecule_synonym", "syn_type",  "alogp", "aromatic_rings",
    "cx_logd", "cx_logp", "cx_most_pka1", "cx_most_pka2", "full_molformula", "full_mwt",
    "hba", "hba_lipinski", "hbd", "hbd_lipinski", "heavy_atoms",
    "molecular_species", "mw_freebase", "mw_monoisotopic", "np_likeness_score",
    "num_lipinski_ro5_violations", "num_ro5_violations", "psa", "qed_weighted",
    "ro3_pass", "rtb", "rotatable_bond_count", "fingerprint", "fingerprint_type",
    "canonical_smiles", "isomeric_smiles", "molfile", "standard_inchi", "standard_inchi_key",
    "cactvs_fingerprint", "cid", "complexity", "conformer_id_3d", "conformer_rmsd_3d", "coordinate_type", "covalent_unit_count", "defined_atom_stereo_count", "defined_bond_stereo_count", "effective_rotor_count_3d", "feature_selfoverlap_3d", "fingerprint", "isotope_atom_count", "iupac_name", "mmff94_energy_3d", "mmff94_partial_charges_3d", "multipoles_3d", "pharmacophore_features_3d", 'charge', "rotatable_bond_count", "shape_fingerprint_3d", "shape_selfoverlap_3d", "tpsa", "undefined_atom_stereo_count", "undefined_bond_stereo_count", "volume_3d", "xlogp"
]

# Create a dictionary with default value 0 for each attribute
global_values = {attr: 0 for attr in global_attributes}



# Mapping between ChEMBL schema and Pubchem schema to Global schema
global_mapping = {
    'drug_id': ['chembl_id' , 'compound_id'],
    'name': ['pref_name' , 'name'],
    'atc_classifications':['atc_classifications', None],
    'availability_type': ['availability_type', None],
    'biotherapeutic': ['biotherapeutic', None],
    'black_box_warning': ['black_box_warning', None],
    'chebi_par_id': ['chebi_par_id', None],
    'chemical_probe': ['chemical_probe', None],
    'chirality': ['chirality', None],
    'cross_references': ['cross_references', None],
    'dosed_ingredient': ['dosed_ingredient', None],
    'first_approval': ['first_approval', None],
    'first_in_class': ['first_in_class', None],
    'helm_notation': ['helm_notation', None],
    'indication_class': ['indication_class', None],
    'inorganic_flag': ['inorganic_flag', None],
    'max_phase': ['max_phase', None],
    'molecule_chembl_id': ['molecule_chembl_id', None],
    'molecule_hierarchy': ['molecule_hierarchy', None],
    'molecule_type': ['molecule_type', None],
    'natural_product': ['natural_product', None],
    'oral': ['oral', None],
    'parenteral': ['parenteral', None],
    'polymer_flag': ['polymer_flag', None],
    'prodrug': ['prodrug', None],
    'structure_type': ['structure_type', None],
    'therapeutic_flag': ['therapeutic_flag', None],
    'topical': ['topical', None],
    'usan_stem': ['usan_stem', None],
    'usan_stem_definition': ['usan_stem_definition', None],
    'usan_substem': ['usan_substem', None],
    'usan_year': ['usan_year', None],
    'withdrawn_flag': ['withdrawn_flag', None],

    'molecule_synonym': ['molecule_synonym', None],
    'syn_type': ['syn_type', None],


    'alogp': ['alogp', None],
    'aromatic_rings': ['aromatic_rings', None],
    'cx_logd': ['cx_logd', None],
    'cx_logp': ['cx_logp', None],
    'cx_most_pka1': ['cx_most_pka1', None],
    'cx_most_pka2': ['cx_most_pka2', None],
    'full_molformula': ['full_molformula', 'formula'], 
    'full_mwt': ['full_mwt', 'molecular_weight'],
    'hba': ['hba', 'h_bond_acceptor_count'],
    'hba_lipinski': ['hba_lipinski', None],
    'hbd': ['hbd', 'h_bond_donor_count'],
    'hbd_lipinski': ['hbd_lipinski', None],
    'heavy_atoms': ['heavy_atoms', 'heavy_atom_count'],
    'molecular_species': ['molecular_species', None],
    'mw_freebase': ['mw_freebase', None],
    'mw_monoisotopic': ['mw_monoisotopic', None],
    'np_likeness_score': ['np_likeness_score', None],
    'num_lipinski_ro5_violations': ['num_lipinski_ro5_violations', None],
    'num_ro5_violations': ['num_ro5_violations', None],
    'psa': ['psa', None],
    'qed_weighted': ['qed_weighted', None],
    'ro3_pass': ['ro3_pass', None],
    'rtb': ['rtb', None],


    'canonical_smiles': ['canonical_smiles', 'canonical_smiles'],  
    'isomeric_smiles' : [None , 'isomeric_smiles'],
    'molfile': ['molfile', None],
    'standard_inchi': ['standard_inchi', 'inchi'],
    'standard_inchi_key': ['standard_inchi_key', 'inchikey'],

    "cactvs_fingerprint": [None, "cactvs_fingerprint"],
    "cid": [None, "cid"],
    "complexity": [None, "complexity"],
    "conformer_id_3d": [None, "conformer_id_3d"],
    "conformer_rmsd_3d": [None, "conformer_rmsd_3d"],
    "coordinate_type": [None, "coordinate_type"],
    "covalent_unit_count": [None, "covalent_unit_count"],
    "defined_atom_stereo_count": [None, "defined_atom_stereo_count"],
    "defined_bond_stereo_count": [None, "defined_bond_stereo_count"],
    "effective_rotor_count_3d": [None, "effective_rotor_count_3d"],
    "feature_selfoverlap_3d": [None, "feature_selfoverlap_3d"],
    "fingerprint": [None, "fingerprint"],
    "isotope_atom_count": [None, "isotope_atom_count"],
    "iupac_name": [None, "iupac_name"],
    "mmff94_energy_3d": [None, "mmff94_energy_3d"],
    "mmff94_partial_charges_3d": [None, "mmff94_partial_charges_3d"],
    "multipoles_3d": [None, "multipoles_3d"],
    "pharmacophore_features_3d": [None, "pharmacophore_features_3d"],
    'charge': [None, 'charge'],
    "rotatable_bond_count": [None, 'rotatable_bond_count'],
    "shape_fingerprint_3d": [None, "shape_fingerprint_3d"],
    "shape_selfoverlap_3d": [None, "shape_selfoverlap_3d"],
    "tpsa": [None, "tpsa"],
    "undefined_atom_stereo_count": [None, "undefined_atom_stereo_count"],
    "undefined_bond_stereo_count": [None, "undefined_bond_stereo_count"],
    "volume_3d": [None, "volume_3d"],
    "xlogp": [None, "xlogp"]
    
}




# def tranform(chembl_values , pubchem_values , gloabl_values, global_mapping ):



