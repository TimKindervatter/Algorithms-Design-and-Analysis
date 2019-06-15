import heapq
from pathlib import Path
from UnionFind import UnionFind


def cluster(adj_list, n, k):
    """Creates k clusters of the n points listed in the provided adjacency list."""

    # Union-find data structure to represent clusters
    parents = [i for i in range(1, n+1)]
    # ranks = {i: 0 for i in range(1, n+1)}
    clusters = UnionFind(parents)

    # Heap for quick access of minimum separation
    priority_tuples = [priority_tuple(edge) for edge in adj_list]
    heapq.heapify(priority_tuples)

    min_separation, endpoints = heapq.heappop(priority_tuples)
    while n > k:
        if clusters.find(endpoints[0]) != clusters.find(endpoints[1]):
            clusters.union(endpoints[0], endpoints[1])

            while clusters.find(endpoints[0]) == clusters.find(endpoints[1]):
                min_separation, endpoints = heapq.heappop(priority_tuples)

            n -= 1

    return min_separation


def priority_tuple(edge):
    return (edge[2], [edge[0], edge[1]])


if __name__ == '__main__':
    path = Path(__file__ + '../..').resolve()
    adj_list = []
    with open(Path(path, 'clustering1.txt')) as file:
        for line in file:
            adj_list.append([int(x) for x in line.split()])

    n = adj_list.pop(0)[0]
    min_separation = cluster(adj_list, n, 4)

    print(min_separation)