from flask import Flask, render_template, request, redirect, session
from query import get_drug_info_chembl , get_drug_info_pubchem , get_drug_from_Unichem
from global_schema import making_global_schema , schema_mapping
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
        # Store the data in a session
        session["input_type"] = input_type
        session["input_data"] = input_data
 
        print(input_type , input_data)
        if(input_type == "drug_name"): 
            # module_name = 'query'
            # function_names = ['get_drug_info_chembl', 'get_drug_info_pubchem']

            # data_sources = {}
            # for function_name in function_names:
            #     data_sources[function_name] = {"module": module_name, "function": function_name}
            data_sources = {
                "chembl": {"module": 'query', "function": "get_drug_info_chembl"},
                "pubchem": {"module": 'query', "function": "get_drug_info_pubchem"},
                # "unichem": {"module": 'query', "function": "get_drug_info_Unichem"},
            }
            session['sources'] = data_sources
            
            for data_source_name,  function_info in data_sources.items():
                module_name = function_info['module']
                function_name = function_info['function']
                module = importlib.import_module(module_name)
                data_function = getattr(module, function_name)
                data = data_function(input_data)
                redis_key = data_source_name
                redis_client.set(redis_key, json.dumps(data))
                # session[data_source_name] = data
                print("Cache stored successfully")
            return redirect("/result")
            
    return render_template("index.html")



@app.route("/result")
def result():
    input_type = session.get("input_type", "No input type")
    input_data = session.get("input_data", "No input data")
    data_sources = session.get("sources", "No input data")
    print(data_sources)

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
            print("Cache retrieved successfully")
    except:
        print("Cache not retrieved successfully")


    
    return render_template("result.html", input_type=input_type, input_data=input_data , assembled_data = assembled_data)


    #drug_info_chembl=drug_info_chembl

    #drug_info_pubchem=assembled_drug_info_pubchem
    #global_values = global_values
    #drug_info_pubchem=assembled_drug_info_pubchem



 
if __name__ == "__main__":
    app.run(debug=True)
