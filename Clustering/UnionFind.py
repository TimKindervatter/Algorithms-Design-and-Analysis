from networkx.utils import groups


class UnionFind:
    def __init__(self, nodes):
        self.parent = {}
        self.rank = {}
        for node in nodes:
            self.parent[node] = node
            self.rank[node] = 0

    def union(self, p, q):
        """ 
        Combines the disjoint subset that contains p with the disjoint subset that contains q.
        Unions are performed by rank. In case of ties, the root of p's subset remains the root of the unioned subset.
        """
        if p == q:
            return

        s1 = self.find(p)
        s2 = self.find(q)

        if self.rank[s1] == self.rank[s2]:
            self.parent[s2] = s1
            self.rank[s1] += 1
        elif self.rank[s1] > self.rank[s2]:
            self.parent[s2] = s1
        elif self.rank[s1] < self.rank[s2]:
            self.parent[s1] = s2

    def find(self, x):
        """ Returns the leader of the disjoint subset containing x."""
        root = self.parent[x]

        while self.parent[root] != root:
            self.parent[root] = self.parent[self.parent[root]]  # Path compression
            root = self.parent[root]

        return root

    def __str__(self):
        """ The union-find is represented as a list of disjoint subsets."""
        subsets = sorted(map(sorted, self.get_subsets()))
        return str(subsets)

    def __len__(self):
        return len(self.get_subsets())

    def get_subsets(self):
        """ Groups elements by the subset they belong to and returns a list of all subsets."""
        return list(groups(self.parent).values())

