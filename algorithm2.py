
class UnionFind:
    def __init__(self, n):
        self.parent =list(range(n))
        self.rank = [0] * n  

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(n, edges):
    
    
    
    edges.sort()
    
    uf = UnionFind(n)  
    mst = []  
    mst_weight = 0  

    # 2. التعامل مع الحواف
    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):  
            uf.union(u, v)  
            mst.append((u, v, weight))  
            mst_weight += weight

    return mst, mst_weight

edges = [
    (10, 0, 1),
    (15, 0, 2),
    (5, 1, 2),
    (10, 1, 3),
    (20, 2, 3)
]


n = 4

mst, mst_weight = kruskal(n, edges)


print("edges in MST:")
for u, v, weight in mst:
    print(f"({u}, {v}) - edge weight {weight}")
print(f"total weight of MST: {mst_weight}")