import random
from pathlib import Path
from graph import Weighted_Graph

def prim(adj_list):
    G = Weighted_Graph(adj_list)
    MST = find_MST(G)
    MST_cost = calculate_MST_cost(MST)

    return MST_cost


def find_MST(graph):
    starting_node = 1

    X = set()
    X.add(starting_node)
    V = set(graph.tail_nodes + graph.head_nodes)
    MST = []

    while not X == V:
        outgoing_edges = []
        for edge in graph.edges:
            if (edge_tail(edge) in X and edge_head(edge) not in X):
                outgoing_edges.append(edge)
            elif (edge_head(edge) in X and edge_tail(edge) not in X):
                outgoing_edges.append(edge)
        cheapest_edge = find_cheapest_edge(outgoing_edges)
        MST.append(cheapest_edge)

        X.add(edge_head(cheapest_edge))
        X.add(edge_tail(cheapest_edge))

    return MST


def find_cheapest_edge(outgoing_edges):
    return min(outgoing_edges, key=lambda x: x[2])


def edge_tail(edge):
    return edge[0]


def edge_head(edge):
    return edge[1]


def edge_without_weight(cheapest_edge):
    weightless_edge = (cheapest_edge[0], cheapest_edge[1])
    return weightless_edge


def calculate_MST_cost(MST):
    weights = [edge[2] for edge in MST]
    return sum(weights)


if __name__ == '__main__':
    path = Path(__file__ + '../..').resolve()

    data = []
    with open(Path(path, "edges.txt")) as file:
        for line in file:
            data.append([int(x) for x in line.strip().split()])

    adj_list = data[1:]
    MST_cost = prim(adj_list)

    print(MST_cost)