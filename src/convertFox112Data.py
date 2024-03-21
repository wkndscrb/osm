import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            data.append(row)

    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

csv_to_json('./data/WES.csv', './data/WES.json')
