import numpy as np
from pathlib import Path


def knapsack(knapsack_capacity, items):
    num_items = len(items)
    values = []
    weights = []

    for item in items:
        values.append(get_item_value(item))
        weights.append(get_item_weight(item))

    A = np.zeros([num_items+1, knapsack_capacity+1], dtype=np.int)

    # for x in range(knapsack_capacity):
    #     A[0, x] = 0

    for i in range(num_items):
        for x in range(knapsack_capacity+1):
            if weights[i] > x:
                A[i+1, x] = A[i, x]
            else:
                A[i+1, x] = max(A[i, x], A[i, x-weights[i]] + values[i])

    return A[num_items, knapsack_capacity]


def get_item_value(item):
    return item[0]


def get_item_weight(item):
    return item[1]


def read_input(filename):
    with open(filename) as f:
        first_line = f.readline().strip().split()
        knapsack_capacity = int(first_line[0])

        items = []
        for line in f.readlines():
            items.append([int(x) for x in line.strip().split()])

    return knapsack_capacity, items


def read_output(filename):
    with open(filename) as f:
        answer = int(f.readline().strip())

    return answer


if __name__ == '__main__':
    path = Path(__file__ + '../..').resolve()
    filename = Path(path, 'knapsack1.txt')

    knapsack_capacity, items = read_input(filename)

    A = knapsack(knapsack_capacity, items)
    print(A)