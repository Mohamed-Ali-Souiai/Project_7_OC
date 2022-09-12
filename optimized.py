import csv
import sys

sys.setrecursionlimit(1050)
som = 0
list_action = []
capacity = 500
with open('data_base/dataset3_Python+P7.csv', newline='') as file:
    data = csv.reader(file)
    for action in data:
        if action[1] != 'price' and action[2] != 'profit':

            action[1] = int(float(action[1]))
            action[2] = action[1] * float(action[2])
            list_action.append(list(action))

"""list_action = sorted(
    list_action, key=lambda x: x[1], reverse=False)"""

"""for line in list_action:
    print(line)"""


# Solution optimale - programmation dynamique
def sacADos_dynamique(capacity, list_action):
    matrice = [[0 for x in range(capacity + 1)] for x in range(len(list_action) + 1)]

    for i in range(1, len(list_action) + 1):
        for w in range(1, capacity + 1):
            if list_action[i-1][1] <= w:
                matrice[i][w] = max(
                    list_action[i-1][2] + matrice[i-1][w-list_action[i-1][1]],
                    matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # Retrouver les éléments en fonction de la somme
    w = capacity
    n = len(list_action)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = list_action[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]

        n -= 1

    return matrice[-1][-1], elements_selection


results = sacADos_dynamique(capacity, list_action)
for profit in results[1]:
    print(profit)
    som += profit[2]
print(f"Bénéfice :{som}")
