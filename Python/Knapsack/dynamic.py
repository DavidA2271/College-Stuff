

def dynamic_programming(bag, weight_limit):
    bag_size = len(bag) + 1
    matrix = [ [0] * (weight_limit + 1) for n in range(bag_size)]
    for i in range(1, bag_size):
        value = bag[i-1][0]
        weight = bag[i-1][1]
        for w in range(weight_limit + 1):
            remainder = w - weight
            current_val = 0
            leftover = 0
            if weight <= w:
                current_val = value
                leftover = matrix[i-1][remainder]
            if matrix[i-1][w] > current_val + leftover:
                matrix[i][w] += matrix[i-1][w]
                remainder = 0
            else:
                matrix[i][w] += current_val
            if remainder > 0:
                matrix[i][w] += matrix[i-1][remainder]
    index = -1
    items = []
    matrix.reverse()
    for j in range(len(matrix)):
        cur_val = matrix[j][index]
        if j == len(matrix)-1:
            break
        if cur_val != matrix[j+1][index]:
            items.append(bag[bag_size-j-2])
            index -= bag[bag_size-j-2][1]
    return items