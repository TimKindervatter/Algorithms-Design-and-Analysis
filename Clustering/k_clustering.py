import heapq
from UnionFind import UnionFind


def cluster(adj_list, n, k):
    """Creates k clusters of the n points listed in the provided adjacency list."""

    # Union-find data structure to represent clusters
    parents = {i: {i} for i in range(1, n+1)}
    ranks = {i: 0 for i in range(1, n+1)}
    clusters = UnionFind(parents, ranks)

    # Heap for quick access of minimum separation
    priority_tuples = [priority_tuple(edge) for edge in adj_list]
    heap = heapq.heapify(priority_tuples)

    while n > k:
        _, endpoints = heapq.heappop(heap)
        if clusters.parent[endpoints[0]] != clusters.parent[endpoints[1]]:
            clusters.union(endpoints[0], endpoints[1])
            n -= 1
        else:
            continue

    min_separation, _ = heapq.heappop(heap)

    return min_separation


def priority_tuple(edge):
    return (edge[2], [edge[0], edge[1]])


# def merge(clusters, endpoints):
#     a = endpoints[0]
#     b = endpoints[1]

#     #This won't work, would need to update all keys which would be O(n)
#     #TODO: Use a Union-Find
#     clusters[a] = clusters[a].union(clusters[b])
#     clusters[b] = clusters[b].union(clusters[a])

#     return clusters