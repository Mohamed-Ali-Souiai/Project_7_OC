import csv
from itertools import combinations
# import sys

# sys.setrecursionlimit(1050)
som = 0
list_action = []
capacity = 50000
database = 'data_base/dataset1_Python+P7.csv'

def extract_csv_data(data):

    with open(data) as file:
        actions = csv.reader(file, delimiter=',')
        next(file)       # ignor first line
        actions_taken = []
        for action in actions:
            if float(action[1]) <= 0 or float(action[2]) <= 0:
                pass
            else:
                take = (
                    action[0],
                    int(float(action[1])*100),
                    float(action[1]) * float(action[2])
                )
                actions_taken.append(take)

        return actions_taken


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

list_action= extract_csv_data(database)
"""for item in list_action:
    print(item)
input('pause')"""
result = bruteforce(list_action)
print(len(result))
for item in result:
    print(item)
print("{:.2f}".format(sum([i[2]for i in result])))
print("{:.2f}".format(sum([i[1]for i in result])/100))
