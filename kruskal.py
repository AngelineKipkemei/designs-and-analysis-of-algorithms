import heapq

# Union-Find Data Structure (Disjoint Set Union)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

# Kruskal's Algorithm for MST
def kruskal(n, edges):
    uf = UnionFind(n)
    mst = []
    edges.sort(key=lambda x: x[2])  # Sort edges by weight (cost)

    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))

    return mst

# Example Graph (vertices = 0, 1, 2, 3)
edges = [
    (0, 1, 10), (0, 2, 6), (0, 3, 5),
    (1, 3, 15), (2, 3, 4)
]

# Number of vertices
n = 4

# Get Minimum Spanning Tree
mst = kruskal(n, edges)

print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"Edge ({u}, {v}) with cost {weight}")
