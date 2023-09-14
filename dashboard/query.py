import pubchempy as pcp

def get_drug_info_pubchem(name):
    try:
        # Search for the compound by name or identifier
        compounds = pcp.get_compounds(name, 'name')
        
        if not compounds:
            print(f"No compound found for '{name}'")
            return
        
        for compound in compounds:
            print(f"Compound Name: {compound.synonyms[0]}")
            print(f"PubChem CID: {compound.cid}")
            print(f"Formula: {compound.molecular_formula}")
            print(f"IUPAC Name: {compound.iupac_name}")
            
            # Print additional properties if available
            if compound.molecular_weight:
                print(f"Molecular Weight: {compound.molecular_weight}")
            if compound.canonical_smiles:
                print(f"SMILES Notation: {compound.canonical_smiles}")
            if compound.inchi:
                print(f"InChI: {compound.inchi}")
            
            print("\n")  # Add a separator between compound entries

    except Exception as e:
        print("Error:", str(e))

# Example usage:
name = "Aspirin"
get_drug_info_pubchem(name)
