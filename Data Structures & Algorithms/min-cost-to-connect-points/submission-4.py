class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        groups = len(points)
        size = [1]*groups
        parent = list(range(groups))
        distance = []
        for i in range(groups):
            for j in range(i+1,groups):
                xi,yi = points[i]
                xj,yj = points[j]
                distance.append((abs(xi-xj)+abs(yi-yj), i,j))
        distance.sort()
        def find(node):
            while parent[node]!=node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        ans = 0
        for d, pi, pj in distance:
            ppi = find(pi)
            ppj = find(pj)
            if ppi!=ppj:
                ans += d
                groups-=1
                if size[ppi]>size[ppj]:
                    parent[ppj]=ppi
                    size[ppi]+=size[ppj]
                else:
                    parent[ppi]=ppj
                    size[ppj]+=size[ppi]
                if groups==1:
                    break
        return ans