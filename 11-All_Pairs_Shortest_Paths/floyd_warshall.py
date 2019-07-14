import numpy as np


def floyd_warshall(adj_list, n):
    def edge_present(i, j):
        return adj_list.get((i, j))

    A = np.full([n+1, n+1, n+1], np.inf)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                A[i, j, 0] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if edge_present(i, j):
                A[i, j, 0] = adj_list[i, j]

    for k in range(1, n+1):
        print(k)
        for i in range(1, n+1):
            for j in range(1, n+1):
                A[i, j, k] = min(A[i, j, k-1], A[i, k, k-1] + A[k, j, k-1])

    negative_cycle_present = detect_negative_cycles(A, n)

    if not negative_cycle_present:
        return A[:, :, -1].min()
    else:
        return "NULL"


def detect_negative_cycles(A, n):
    for i in range(n):
        if A[i, i, n] < 0:
            return True
        
    return False


def read_input(filename):
    adj_list = {}
    with open(filename) as f:
        n, m = (int(x) for x in f.readline().split())
        for line in f.readlines():
            row = line.split()
            tail_node = int(row[0])
            head_node = int(row[1])
            edge_length = int(row[2])

            # Handle parallel edges
            if adj_list.get((tail_node, head_node)):
                # If an edge already exists between the current node pair, only use the one with minimum edge length
                new_value = min(adj_list[tail_node, head_node], edge_length)
                adj_list[tail_node, head_node] = new_value
            else:
                adj_list[tail_node, head_node] = edge_length

    return adj_list, n


def read_output(filename):
    with open(filename) as f:
        line = f.readline().strip()
        try:
            answer = int(line)
        except ValueError:
            answer = line

    return answer


if __name__ == '__main__':
    # adj_list_1, n_1 = read_input('g1.txt')
    # adj_list_2, n_2 = read_input('g2.txt')
    adj_list_3, n_3 = read_input('g3.txt')

    # print("Starting graph 1")
    # A_1 = floyd_warshall(adj_list_1, n_1)
    # print("Starting graph 2")
    # A_2 = floyd_warshall(adj_list_2, n_2)
    print("Starting graph 3")
    A_3 = floyd_warshall(adj_list_3, n_3)
    
    # print(A_1)
    # print(A_2)
    print(A_3)
