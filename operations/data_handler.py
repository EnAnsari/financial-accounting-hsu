import json

def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return data['members'], data['records']
    except FileNotFoundError:
        # Handle the case where the file doesn't exist (optional: create an empty file)
        return [], []

def save_data(members, records):
    data = {
        'members': members,
        'records': records,
    }
    with open('data.json', 'w') as file:
        json.dump(data, file)
