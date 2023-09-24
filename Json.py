import json
# with open('Mohamed.json', 'w') as f:
#     json.dump(infos, f, indent = 4)

# Convert Json File into Dictionary Using Loads function 
infos = {
    "firstName": "Mohamed",
    "lastName": "Ouahlou",
    "Age": 22,
    "Gender": "Male",
    "Level": "BAC+4",
    "IsSingle": "Yes",
    "Skills": [
        "Data analyst",
        "Python",
        "SQL",
        "Excel"
    ]
}

person = json.dumps(infos)

# infos_js = json.dumps(infos, indent= 4)
# print(infos_js)

mohamed = json.loads(person)
print(mohamed)