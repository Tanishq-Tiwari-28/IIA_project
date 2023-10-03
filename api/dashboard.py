from flask import Flask, render_template, request, redirect, session
from query import get_drug_info_chembl , get_drug_info_pubchem  
import json
import redis
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random, secure key

redis_client = redis.Redis(host='localhost', port=6379, db=0)

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
            drug_info_pubchem = get_drug_info_pubchem(input_data)
            print(type(drug_info_pubchem))
            redis_client.set("drug_info_pubchem", json.dumps(drug_info_pubchem))
            # chunk_size = 500 # Adjust the chunk size based on browser limitations
            # chunks = [drug_info_pubchem[i:i + chunk_size] for i in range(0, len(drug_info_pubchem), chunk_size)]
            # for i, chunk in enumerate(chunks):
            #     cookie_name = f"drug_info_pubchem_chunk_{i}"
            #     session[cookie_name] = json.dumps(chunk)
            drug_info_chembl , global_values = get_drug_info_chembl(input_data)
            session["drug_info_chembl"] = drug_info_chembl
            session["global_values"] = global_values
            return redirect("/result")
            
    return render_template("index.html")



@app.route("/result")
def result():
    input_type = session.get("input_type", "No input type")
    input_data = session.get("input_data", "No input data")
    drug_info_chembl = session.get("drug_info_chembl", "No Drug Found")
    global_values = session.get("global_values", "No Drug Found")

    # drug_info_pubchem = session.get("drug_info_pubchem", "No Drug Found")
    # assembled_drug_info_pubchem = {}
    # chunk_index = 0
    # while True:
    #     cookie_name = f"drug_info_pubchem_chunk_{chunk_index}"
    #     chunk_data = session.get(cookie_name)
    #     if chunk_data:
    #         chunk = json.loads(chunk_data)
    #         assembled_drug_info_pubchem.update(chunk)
    #         chunk_index += 1
    #     else:
    #         break

    # Remove the session data
    # for i in range(chunk_index):
    #     cookie_name = f"drug_info_pubchem_chunk_{i}"
    #     session.pop(cookie_name, None)

    drug_info_pubchem_json = redis_client.get("drug_info_pubchem")
    if drug_info_pubchem_json:
        assembled_drug_info_pubchem = json.loads(drug_info_pubchem_json)
    else:
        assembled_drug_info_pubchem = {}
    # print("dhsfghsfgh",assembled_drug_info_pubchem) 
    session.pop("drug_info_chembl", None)
    print(global_values)
    return render_template("result.html", input_type=input_type, input_data=input_data , drug_info_chembl=drug_info_chembl ,drug_info_pubchem=assembled_drug_info_pubchem , global_values = global_values) 

    #drug_info_pubchem=assembled_drug_info_pubchem



 
if __name__ == "__main__":
    app.run(debug=True)
