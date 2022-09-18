import json

data = '''{
    "name"  : "Chuck",
    "phone" : {
        "type"   : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

# here json module returns info as a dictionary
info = json.loads(data)
print(len(info))
print(info["name"])
print(info["email"]["hide"])