def cluster(adj_list, n k):
"""Creates k clusters of the n points listed in the provided adjacency list."""

    #TODO: Replace dict with Union-Find
    clusters = {i:{i} for i in range(1, n+1)}
    priority_tuples = [priority_tuple(edge) for edge in adj_list]

    heap = heapify(priority_tuples)

    while len(clusters) > k:
        edge_weight, endpoints = heappop(heap)
        clusters = merge(clusters, endpoints)
        #Find minimum distance among p, q in different clusters


def priority_tuple(edge):
    return (edge[2], [edge[0], edge[1]])


def merge(clusters, endpoints):
    a = endpoints[0]
    b = endpoints[1]

    #This won't work, would need to update all keys which would be O(n)
    #TODO: Use a Union-Find
    clusters[a] = clusters[a].union(clusters[b])
    clusters[b] = clusters[b].union(clusters[a])

    return clusters