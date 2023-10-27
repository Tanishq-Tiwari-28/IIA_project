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
        # print(len(pubchem_attributes))

        pubchem_values = {attr: 0 for attr in pubchem_attributes}

        for attr in pubchem_attributes:
            for info_dict in drug_info_list:
                if attr in info_dict:
                    pubchem_values[attr] = info_dict[attr]
                    break
          
        # print((pubchem_values))

        # print(is_serializable(pubchem_values))
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
        molecule_properties = drug_info.get('molecule_properties')
        molecule_structures = drug_info.get('molecule_structures')
        # molecule_synonym = drug_info.get('molecule_synonyms')

    
        chembl_attributes = list(drug_info.keys()) + list(molecule_properties.keys()) + list(molecule_structures.keys())
        
        # print((chembl_attributes))
        # print(len(chembl_attributes))

        chembl_values = {attr: 0 for attr in chembl_attributes}


        for attr in chembl_attributes:
            if attr in drug_info:
                chembl_values[attr] = drug_info[attr]
        for attr in chembl_attributes:
            if attr in molecule_properties:
                chembl_values[attr] = molecule_properties[attr]
        for attr in chembl_attributes:
            if attr in molecule_structures:
                chembl_values[attr] = molecule_structures[attr]




        print(len(drug_info))
        print(is_serializable(drug_info))

        # print((drug_info))

        return chembl_values
    except Exception as e:
        return "Error: " + str(e)


def get_drug_info_unichem(inchi_key):
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
    print((data_dict.keys()))
    return data_dict



# get_drug_from_unichem("BNRNXUUZRGQAQC-UHFFFAOYSA-N" , '') 

