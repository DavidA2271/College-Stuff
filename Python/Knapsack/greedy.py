


def value_to_weight(bag: list, weight_limit):
    knapsack_capacity = 0
    knapsack_value = 0
    bag.sort(key=lambda x: (x[0]/x[1]), reverse=True)
    #print(bag)
    for item in bag:
        if knapsack_capacity + item[1] <= weight_limit:
            knapsack_value += item[0]
            knapsack_capacity += item[1]
    return (knapsack_value, knapsack_capacity)



def max_value(bag, weight_limit):
    knapsack_capacity = 0
    knapsack_value = 0
    bag.sort(key=lambda x: x[0], reverse=True)
    #print(bag)
    for item in bag:
        if knapsack_capacity + item[1] <= weight_limit:
            knapsack_value += item[0]
            knapsack_capacity += item[1]
    return (knapsack_value, knapsack_capacity)


def min_weight(bag, weight_limit):
    knapsack_capacity = 0
    knapsack_value = 0
    bag.sort(key=lambda x: x[1], reverse=False)
    #print(bag)
    for item in bag:
        if knapsack_capacity + item[1] <= weight_limit:
            knapsack_value += item[0]
            knapsack_capacity += item[1]
    return (knapsack_value, knapsack_capacity)
