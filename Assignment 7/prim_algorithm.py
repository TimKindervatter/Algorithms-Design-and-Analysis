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
    MST = []

    outgoing_edges = graph.edges[starting_node]
    graph.mark_explored(starting_node)

    while not all(graph.explored.values()):
        cheapest_edge = find_cheapest_edge(outgoing_edges)
        graph.mark_explored(edge_head(cheapest_edge))
        MST.append(cheapest_edge)

        outgoing_edges[:] = [edge for edge in outgoing_edges if not (graph.explored[(edge_tail(edge))] and graph.explored[(edge_head(edge))])]

        outgoing_edges += [edge for edge in graph.edges[edge_head(cheapest_edge)] if not graph.explored[edge_head(edge)]]

    return MST


def find_cheapest_edge(outgoing_edges):
    return min(outgoing_edges, key=lambda x: list(x.values()))


def edge_tail(edge):
    return list(edge.keys())[0][0]


def edge_head(edge):
    return list(edge.keys())[0][1]


def edge_without_weight(cheapest_edge):
    [[edge, _]] = cheapest_edge.items()
    return edge


def calculate_MST_cost(MST):
    weights = [int(val) for edge in MST for _,val in edge.items()]
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