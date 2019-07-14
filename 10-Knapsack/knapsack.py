import numpy as np
from pathlib import Path


def knapsack(knapsack_capacity, items):
    num_items = len(items)

    values, weights = zip(*items)

    A = np.zeros([num_items+1, knapsack_capacity+1], dtype=np.int)

    for i in range(num_items):
        for x in range(knapsack_capacity+1):
            if weights[i] > x:
                A[i+1, x] = A[i, x]
            else:
                A[i+1, x] = max(A[i, x], A[i, x-weights[i]] + values[i])

    return A[num_items, knapsack_capacity]


#! Space efficient but not time efficient
def big_knapsack(knapsack_capacity, items):
    num_items = len(items)

    values, weights = zip(*items)

    A = np.zeros([2, knapsack_capacity+1], dtype=np.int)

    for i in range(1, num_items + 1):
        print(i)
        for x in range(knapsack_capacity + 1):
            if weights[i-1] > x:
                A[i % 2, x] = A[(i % 2) ^ 1, x]
            else:
                A[i % 2, x] = max(A[(i % 2) ^ 1, x], A[(i % 2) ^ 1, x-weights[i-1]] + values[i-1])

    return A[num_items % 2, knapsack_capacity]


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


    filename = Path(path, 'knapsack_big.txt')
    knapsack_capacity, items = read_input(filename)
    A = big_knapsack(knapsack_capacity, items)
    print(A)