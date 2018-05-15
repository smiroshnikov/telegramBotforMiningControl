import json

data = {
    'president': {
        'name': "Sergei Miroshnikov",
        'species': "MordorScuko"
    },
    'prime-minister': {
        'name': "Sergei Miroshnikov",
        'species': "MordorScuko"
    }
}

if __name__ == "__main__":
    with open('president.json', 'w') as f:
        json.dump(data, f)
    str_from_json = json.dumps(data, indent=4)
    print(str_from_json)

    with open('president.json', 'r') as f:
        data = json.load(f)
    for k, v in data.items():
        print(k, v)
