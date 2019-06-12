class UnionFind:
    def __init__(self, parents, ranks):
        self.parent = parents
        self.rank = ranks

    def union(self, p, q):
        s1 = self.find(p)
        s2 = self.find(q)

        if self.rank[s1] == self.rank[s2]:
            self.parent[s2] = s1
            self.rank[s2] += 1
        elif self.rank[s1] > self.rank[s2]:
            self.parent[s2] = s1
        elif self.rank[s1] < self.rank[s2]:
            self.parent[s1] = s2
        
        return self.parent

    def find(self, x):
        root = self.parent[x]

        while self.parent[root] != root:
            root = self.parent[root]

        return root