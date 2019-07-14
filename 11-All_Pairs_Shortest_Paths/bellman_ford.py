import numpy as np


def bellman_ford(adj_list, n, source_node):
    A = np.full([n+1, n+1], np.inf)

    tail_nodes = [item[0] for item in adj_list.keys()]
    head_nodes = [item[1] for item in adj_list.keys()]
    V = set(tail_nodes + head_nodes)

    edges_present = {}
    for head_node in set(head_nodes):
        edges_present[head_node] = []
        for tail_node in set(tail_nodes):
            if adj_list.get((tail_node, head_node)) is not None:
                edges_present[head_node].append(tail_node)

    A[0, source_node] = 0
    
    for v in range(n+1):
        if v != source_node:
            A[0, v] = np.inf

    for i in range(1, n+1):
        print(i)
        for v in V:
            old_cost = A[i-1, v]
            old_cost_plus_one_hop = []
            old_cost_plus_cheapest_hop = np.inf
            if edges_present.get(v):
                for w in edges_present[v]:
                    old_cost_plus_one_hop.append(A[i-1, w] + adj_list[(w, v)])
                    old_cost_plus_cheapest_hop = min(old_cost_plus_one_hop)
            A[i, v] = min(old_cost, old_cost_plus_cheapest_hop)

    if np.allclose(A[-1, 1:], A[-2, 1:]):
        return list(A[-1, 1:])
    else:
        return "NULL"
        