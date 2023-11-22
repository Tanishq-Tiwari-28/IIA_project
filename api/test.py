import requests
import pubchempy as pcp
from rdkit import Chem

def pubchem_id_to_drug(pubchem_id):
    from pubchempy import Compound
    comp = Compound.from_cid(pubchem_id)
    drug_name = comp.synonyms[0]
    return drug_name


def chembl_id_to_drug_name(chembl_id):
    from chembl_webresource_client.new_client import new_client
    molecule = new_client.molecule
    mol = molecule.get(chembl_id)
    drug_name = mol["pref_name"]
    return drug_name



def smiles_to_drug(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None

    compound = pcp.get_compounds(smiles, 'smiles')
    if compound:
        return compound[0].to_dict(properties=['synonyms'])['synonyms'][0]
    else:
        return None


# print(chembl_id_to_drug_name('chembl192'))
# print(smiles_to_drug('CCCc1nn(C)c2c(=O)[nH]c(-c3cc(S(=O)(=O)N4CCN(C)CC4)ccc3OCC)nc12'))
print(pubchem_id_to_drug('135398744'))
