from flask import Flask, render_template, request, redirect, session
from query import *
from global_schema import making_global_schema
import json
import redis
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random, secure key

redis_client = redis.Redis(host='localhost', port=6379, db=0)
import importlib
@app.route("/", methods=["GET", "POST"])
def home():
    print('in home')
    if request.method == "POST":
        input_type = request.form["input_type"]
        input_data = request.form["input_data"]
        role = request.form["role"]

        source_add = request.form["source_add"]
        source_remove = request.form["source_remove"]

        # print(source_add , source_remove)

        # Store the data in a session
        session["input_type"] = input_type
        session["input_data"] = input_data
        session['role'] = role
        
        session["source_add"] = source_add
        session["source_remove"] = source_remove

        # print(input_type , input_data)
        data_sources = {
            "chembl": {
                "module": "query",
                "function": "get_drug_info_chembl",
                "search_parameter": "drugname"
            },
            "pubchem": {
                "module": "query",
                "function": "get_drug_info_pubchem",
                "search_parameter": "drugname"
            },
            # "unichem": {
            #     "module": "query",
            #     "function": "get_drug_info_unichem",
            #     "search_parameter": "inchikey"
            # },
        }

        def functions(data_sources):
            search_dict = {}
            data_list = []
            for data_source_name,  function_info in data_sources.items():
                
                module_name = function_info['module']
                function_name = function_info['function']
                search_parameter = function_info['search_parameter']    
                module = importlib.import_module(module_name)
                data_function = getattr(module, function_name)
                print(search_parameter)
                data =  data_function(input_data)
                data_list.append(data)

                if(search_parameter == "inchikey"):
                        data = data_function(search_dict["inchikey"])
                        data_list.append(data) 

                try:
                    if data['molecule_chembl_id'] :
                        search_dict['chembl_id'] = data['molecule_chembl_id']
                    if data['standard_inchi_key'] or data['inchikey']:
                        search_dict['inchikey'] = data['standard_inchi_key']
                        print(search_dict['inchikey'])
                    if data['canonical_smiles']:
                        search_dict['cannonical_smiles'] = data['canonical_smiles']
                except:
                    print("SEARCH DATA NOT STORED")                
                redis_key = data_source_name
                redis_client.set(redis_key, json.dumps(data))
                # session[data_source_name] = data


            global_values = making_global_schema(*data_list)
            redis_key = 'global_data'
            redis_client.set(redis_key, json.dumps(global_values))

        def func2():
            if(source_add == 'NONE' and source_remove =='NONE'):
                functions(data_sources)
                return redirect("/result")
            elif source_add != 'NONE' and source_remove== "NONE":   ##we are adding a mew data source
                print(source_add  , 'is been added')
                if source_add in data_sources:
                    print("REQUIRED DATA SOURCE IS ALREADY PRESENT")
                    functions(data_sources)
                else:
                    data_sources["unichem"] = {
                            "module": "query",
                            "function": "get_drug_info_unichem",
                            "search_parameter": "inchikey"
                        }
                    functions(data_sources)
                    print(source_add  , 'is been added')
                return redirect("/result")  
            elif source_add == 'NONE' and source_remove != "NONE":         ##we are removing a mew data source
                if source_remove in data_sources:
                    data_sources.pop(source_remove)  
                    functions(data_sources)
                    print(source_remove , 'is been removed')
                else:
                    print("REQUIRED DATA SOURCE IS NOT PRESENT")
                return redirect("/result")
            elif source_add != 'NONE' and source_remove != "NONE":  ##we are adding as well removing a new data sources
                print(source_add , 'is been added and ', source_remove , 'is been removed')
        
        
        session['sources'] = data_sources


        if(input_type == "drug_name"):
                func2()
                return redirect("/result")
            
        if(input_type == "chembl_id"):
            drug_name = chembl_id_to_drug_name(input_data)
            input_data = drug_name
            session["input_data"] = input_data
            func2()
            return redirect("/result")
        
        if(input_type == 'smiles'):
            drug_name = smiles_to_drug(input_data)
            input_data = drug_name
            session["input_data"] = input_data
            func2()
            return redirect("/result")
        
        if(input_type == 'pubchem_id'):
            drug_name = pubchem_id_to_drug(input_data)
            input_data = drug_name
            session["input_data"] = input_data
            print("drug name is:   " , input_data)
            func2()
            return redirect("/result")







                
            

              
    return render_template("index.html")



@app.route("/result")
def result():
    input_type = session.get("input_type", "No input type")
    input_data = session.get("input_data", "No input data")
    role = session.get("role", "No input data")

    data_sources = session.get("sources", "No input data")
    # print(data_sources)

    source_add = session.get("source_add")
    source_remove = session.get("source_remove")

    assembled_data = {}
    try:
        for data_source_name in data_sources.keys():
            data_json = redis_client.get(data_source_name)
            # print(data_json)
            if data_json:
                data = json.loads(data_json)
                # print(data)
                if data:
                    assembled_data[data_source_name] = data
            # data_json = session.get(data_source_name)
            # data = json.loads(data_json)
            # assembled_data[data_source_name] = data
            # print("Cache retrieved successfully")
        global_data = redis_client.get('global_data')
        if global_data:
            global_values = json.loads(global_data)
    except:
        print("Cache not retrieved successfully")


    
    return render_template("result.html", input_type=input_type, input_data=input_data , assembled_data = assembled_data , global_values = global_values , source_add = source_add , source_remove=source_remove , role = role)

    # global_values = global_values

    #drug_info_chembl=drug_info_chembl

    #drug_info_pubchem=assembled_drug_info_pubchem
    #global_values = global_values
    #drug_info_pubchem=assembled_drug_info_pubchem



 
if __name__ == "__main__":
    app.run(debug=True)
