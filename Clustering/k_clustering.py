import heapq
from UnionFind import UnionFind


def cluster(adj_list, n, k):
    """Creates k clusters of the n points listed in the provided adjacency list."""

    # Union-find data structure to represent clusters
    parents = {i: i for i in range(1, n+1)}
    ranks = {i: 0 for i in range(1, n+1)}
    clusters = UnionFind(parents, ranks)

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
    adj_list = [
    [1, 2, 10], [1, 3, 12], [1, 4, 6], [1, 5, 11.2], [1, 6, 13],
    [2, 3, 2], [2, 4, 11.7], [2, 5, 5], [2, 6, 5.4],
    [3, 4, 13.4], [3, 5, 5.4], [3, 6, 5],
    [4, 5, 10.05], [4, 6, 12.05],
    [5, 6, 2]]

    clusters = cluster(adj_list, 6, 3)