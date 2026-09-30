class DSU:
    def __init__(self, n):
        self.size = [1]*(n+1)
        self.parent = list(range(n+1))

    def find(self, node):
        while self.parent[node]!=node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self, u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu==pv:
            return False
        if self.size[pu]>self.size[pv]:
            self.size[pu]+=self.size[pv]
            self.parent[pv]=pu
        else:
            self.size[pv]+=self.size[pu]
            self.parent[pu] = pv
        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = []
        for i in range(n):
            for j in range(i+1,n):
                xi,yi = points[i]
                xj,yj = points[j]
                edges.append((abs(xi-xj)+abs(yi-yj), i,j))
        edges.sort()
        ans = 0
        for d,i,j in edges:
            if dsu.union(i,j):
                ans += d
        return ans