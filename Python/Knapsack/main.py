import generator
import greedy
import dynamic
import time


def test_all(items, weight_limit):
    bag = generator.generate_items(items)
    t = time.time()
    greed_ratio = greedy.value_to_weight(bag, weight_limit)
    gr_time = time.time() - t
    t = time.time()
    greed_val = greedy.max_value(bag, weight_limit)
    gv_time = time.time() - t
    t = time.time()
    greed_weight = greedy.min_weight(bag, weight_limit)
    gw_time = time.time() - t
    t = time.time()
    dynamic_val = dynamic.dynamic_programming(bag, weight_limit)
    d_time = time.time() - t
    print(f'In a test with {items} items and a max capacity of {weight_limit}:')
    print()
    print(f'Greed Value to Weight Ratio produced a bag with {greed_ratio[0]} value and {greed_ratio[1]} weight in {gr_time} seconds.')
    print(f'Greed Maximum Value produced a bag with {greed_val[0]} value and {greed_val[1]} weight in {gv_time} seconds.')
    print(f'Greed Minimum Weight produced a bag with {greed_weight[0]} value and {greed_weight[1]} weight in {gw_time} seconds.')
    print()
    print(f'Dynamic Programming produced a bag with {sum(x[0] for x in dynamic_val)} value and {sum(x[1] for x in dynamic_val)} weight in {d_time} seconds.')
    print()
    print()
    print('--------------------------------------------------------------------------------')


test_all(10, 50)
test_all(50, 100)
test_all(100, 200)
