from flask import Flask, render_template, request, redirect, session
# from query import name_chembl   
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random, secure key


def name_chembl(name):
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
        print("Name:", drug_info.get('pref_name'))
        if 'molecule_synonyms' in drug_info:
            synonyms = [synonym['synonyms'] for synonym in drug_info['molecule_synonyms']]
            print("Synonyms:")
            for synonym in synonyms:
                print(f"- {synonym}")
        else:
            print("Synonyms not available for this drug.")
        
    except Exception as e:
        return "Error: " + str(e)


@app.route("/", methods=["GET", "POST"])
def home():
    print('in home')
    if request.method == "POST":
        input_type = request.form["input_type"]
        input_data = request.form["input_data"]
        # Store the data in a session
        session["input_type"] = input_type
        session["input_data"] = input_data
        print(input_type , input_data)
        if(input_type == "drug_name"):
            name_chembl(input_data)         
        return redirect("/result")
    return render_template("index.html")



@app.route("/result")
def result():
    input_type = session.get("input_type", "No input type")
    input_data = session.get("input_data", "No input data")
    return render_template("result.html", input_type=input_type, input_data=input_data)



 
if __name__ == "__main__":
    app.run(debug=True)
