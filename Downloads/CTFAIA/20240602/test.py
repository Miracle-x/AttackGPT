import json


def read_jsonl(file_path):
    i = 0
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            i += 1
            try:
                data.append(json.loads(line))
            except:
                print(i)
    return data


data = read_jsonl('test/metadata.jsonl')
data1 = read_jsonl('validation/metadata.jsonl')
data = data + data1

dict = {}
for t in data:
    dict[t['task_name']] = t['Level']




print(len(dict.keys()))
print(dict)
