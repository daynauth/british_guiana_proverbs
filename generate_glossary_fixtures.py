import csv
import json

list = []

model = "base.entry"

with open('./data/glossary.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        entry = {
            "model": model,
            "fields": {
                "english": row[1],
                "creole": row[0]
            }
        }
        list.append(entry)

output = json.dumps(list, indent=4)

with open('./fixtures/glossary.json', 'w') as f:
    f.write(output)


