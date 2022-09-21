import csv
from itertools import combinations
# import sys

# sys.setrecursionlimit(1050)
som = 0
list_action = []
capacity = 500
with open('data_base/dataset3_Python+P7.csv', newline='') as file:
    data = csv.reader(file)
    for action in data:
        if action[1] != 'price' and action[2] != 'profit':
            action[1] = float(action[1])
            action[2] = action[1] * float(action[2])
            list_action.append(list(action))


def bruteforce(actions):
    selected_item = []
    for i in range(1, len(actions)):
        elements = combinations(actions, i)
        for item in elements:
            if sum([i[1] for i in item]) <= capacity:
                local = sum([i[2] for i in item])
                previous = sum([i[2] for i in selected_item])
                if local > previous:
                    selected_item = item
    return selected_item


result = bruteforce(list_action)
for item in result:
    print(item)
print("{:.2f}".format(sum([i[2]for i in result])))
print("{:.2f}".format(sum([i[1]for i in result])))
