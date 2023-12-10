import csv

file1 = 'proverbs1.txt'
file2 = 'proverbs2.txt'

def clean_data(data: list[str]) -> list[str]:
    data = [line.strip() for line in data]
    data = [line.strip('\"') for line in data]
    data = [line.strip('"') for line in data]
    data = [line for line in data if line != '']
    data = [line.rstrip('.') for line in data]
    data = [line.replace("\\", "") for line in data]
    data = [int(line) if line.isnumeric() else line for line in data]
    return data


with open(file1, 'r') as f:
    lines = f.readlines()

lines = clean_data(lines)


output: dict[int, dict[str, int | str]] = dict(dict())

for i in range(0, len(lines), 2):
    if type(lines[i]) == int and type(lines[i+1]) == str:
        entry: dict[str, int | str] = {'id': lines[i], 'text': lines[i+1]}
        output[int(lines[i])] = entry
    else:
        print("something went wrong")
        print(lines[i])
        exit(1)

with open(file2, 'r') as f:
    lines2 = f.readlines()

lines2 = clean_data(lines2)
lines2 = [line.split(".", 1) for line in lines2]
lines2 = [[line[0].replace(",", ""), line[1]] for line in lines2]


lines2[0] = ['505', 'Jango beg, jango kill']

for i, line in enumerate(lines2):
    if line[0].isnumeric():
        lines2[i] = [int(line[0]), line[1].strip()]
        entry = {'id': lines2[i][0], 'text': lines2[i][1]}
        output[int(lines2[i][0])] = entry
    else:
        print(line)
        exit(1)

print(lines2)


def my_quoting(value):
    #return f'"{value}"' if isinstance(value, str) else value
    return value.strip('"')


with open('./data/proverbs.csv', 'w', newline='', ) as csvfile:
    fieldnames = ['id', 'text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC)

    writer.writeheader()
    for key, entry in output.items():
        row_data = {'id': key, 'text': my_quoting(entry['text'])}
        writer.writerow(row_data)

