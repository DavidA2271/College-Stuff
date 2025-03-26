import random


def generate_items(num_items, max_value=100, max_weight=50):
    items = []
    for i in range(num_items):
        value = random.randint(1, max_value)
        weight = random.randint(1, max_weight)
        items.append((value, weight))
    return items
