import pandas as pd
import pickle
import csv
import json

res = 'outputs/test_with_val.pickle'
with open(res, 'rb') as f:
    x = pickle.load(f)[0]

print(x.shape)

ll = []
with open('data/test.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for i, line in enumerate(csvFile):
        file = line[0].split()[0]
        id = file.split('.')[0].split('/')[-1]
        if x[i][0]>x[i][1]:
            label = False
        else:
            label = True
        ll.append({"unique_id":id, "state_change": label})
        print(i, id, label, x[i])

print(ll)

json_string = json.dumps(ll)
with open('data/submission2.json', 'w') as outfile:
    outfile.write(json_string)

# with open('data/submission2.json', 'r') as f:
#     data = json.load(f)
#     #print(data)
#
# for item in data:
#     id = item['unique_id']
#     label = 1 if item['state_change'] else 0
#     print(id, label)





