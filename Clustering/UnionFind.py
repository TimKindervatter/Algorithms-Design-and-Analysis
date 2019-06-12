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

    # def get_parent(self, x):
    #     return self.parents[x]

    # def set_parent(self, x, new_parent):
    #     self.parents[x] = new_parent
    #     return self.parents

if __name__ == '__main__':
    parents, ranks, p, q, expected = ({1:1, 2:1, 3:1, 4:4, 5:4, 6:4}, {1:1, 2:0, 3:0, 4:1, 5:0, 6:0}, 1, 4, {1:4, 2:1, 3:1, 4:4, 5:4, 6:4})

    clusters = UnionFind(parents, ranks)
    new_parents = clusters.union(p, q)

    assert(new_parents == expected)