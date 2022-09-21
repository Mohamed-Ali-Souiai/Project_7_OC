import csv


sum_profit = 0
sum_price = 0
capacity = 500
all_actions = []
data_base = 'data_base/dataset1_Python+P7.csv'
def extract_csv_data(data):

    with open(data) as file:
        actions = csv.reader(file, delimiter=',')
        next(file)       # ignor first line
        list_action = []
        for action in actions:
            if float(action[1]) <= 0 or float(action[2]) <= 0:
                pass
            else:
                take = (
                    action[0],
                    int(float(action[1])*100),
                    float(action[1]) * float(action[2])
                )
                list_action.append(take)

        return list_action
 
 
def knapsack(capacity, price, profit, length):
    K = [[0 for x in range(capacity + 1)] for x in range(length + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(length + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif price[i-1] <= w:
                K[i][w] = max(profit[i-1]
                          + K[i-1][w-price[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    # Retrouver les éléments en fonction de la somme
    
    #list_action = all_actions
    elements_selection = []

    while capacity >= 0 and length >= 0:
        e = all_actions[length-1]
        if K[length][capacity] == K[length-1][capacity-e[1]] + e[2]:
            elements_selection.append(e)
            capacity -= e[1]

        length -= 1

    return K[-1][-1]/100, elements_selection
 
 
def part():
    all_actions = extract_csv_data(data_base)
    price = []
    profit = []
    for action in all_actions:
        price.append(action[1])
        profit.append(action[2])
    return price,profit,all_actions

price, profit, all_actions = part()

results = knapsack(100*capacity, price, profit, len(profit))
for profit in results[1]:
    print(profit)
    sum_profit += profit[2]
    sum_price += profit[1]

if data_base == 'data_base/dataset3_Python+P7.csv':
    print(f"profit :{sum_profit :.2f} \nprice :{sum_price/100 :.2f}")
else:
    print(f"profit :{sum_profit/100 :.2f} \nprice :{sum_price/100 :.2f}")
