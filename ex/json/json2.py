import json

input = '''[
    {   "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {   "id" : "009",
        "x" : "7",
        "name" : "Chuck"
    }
]'''

data = json.loads(input)

for item in data :
    print(item["id"], item["name"], item["x"])




