import json

json_string = '{"name": "Akhil", "age": 20}'

data = json.loads(json_string)

if isinstance(data, (dict, list)):
    print("The JSON string contains a complex object.")
else:
    print("The JSON string does not contain a complex object.")