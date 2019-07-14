from bellman_ford import bellman_ford
from floyd_warshall import read_input, read_output

def johnson(adj_list, n, source_node):
    tail_nodes = [item[0] for item in adj_list.keys()]
    head_nodes = [item[1] for item in adj_list.keys()]
    V = set(tail_nodes + head_nodes)

    for v in V:
        adj_list[(source_node, v)] = 0

    A = bellman_ford(adj_list, n, source_node)

    if type(A) == str:
        return A
    else:
        return min(A)


if __name__ == '__main__'
    source_node = 0
    adj_list_1, n_1 = read_input('g1.txt')
    adj_list_2, n_2 = read_input('g2.txt')
    adj_list_3, n_3 = read_input('g3.txt')

    print("Starting graph 1")
    A_1 = johnson(adj_list_1, n_1, source_node)
    print("Starting graph 2")
    A_2 = johnson(adj_list_2, n_2, source_node)
    print("Starting graph 3")
    A_3 = johnson(adj_list_3, n_3, source_node)
    
    print(A_1)
    print(A_2)
    print(A_3)