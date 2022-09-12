import csv

som = 0
list_action = []
capacity = 500
with open('data_base/dataset3_Python+P7.csv', newline='') as file:
    data = csv.reader(file)
    for action in data:
        if action[1] != 'price' and action[2] != 'profit':
            action[1] = int(action[1])
            action[2] = action[1] * float(action[2])
            list_action.append(list(action))


# Solution force brute - Recherche de toutes les solutions
def sacados_force_brute(capacity_max, actions, elements_selection=[]):
    if actions:
        val1, lst_val = sacados_force_brute(capacity_max, actions[1:], elements_selection)
        val = actions[0]
        if val[1] <= capacity_max:
            val2, lst_val = sacados_force_brute(capacity_max - val[1], actions[1:], elements_selection + [val])
            if val1 < val2:
                return val2, lst_val

        return val1, lst_val
    else:
        return sum([i[2] for i in elements_selection]), elements_selection


results = sacados_force_brute(capacity, list_action)
for profit in results[1]:
    print(profit)
    som += profit[2]
print(len(results[1]))
print(f"Bénéfice :{som}")
print(f"Bénéfice :{results}")
