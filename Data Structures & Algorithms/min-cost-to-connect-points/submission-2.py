class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hmap = {}
        groups = 0
        for x,y in points:
            hmap[(x,y)] = groups
            groups+=1
        size = [1]*groups
        cost = [0]*groups
        parent = []
        for i in range(groups):
            parent.append(i)
        distance = []
        for i in range(groups):
            for j in range(i+1,groups):
                xi,yi = points[i]
                xj,yj = points[j]
                distance.append((abs(xi-xj)+abs(yi-yj), hmap[(xi,yi)], hmap[(xj,yj)]))
        distance.sort(reverse = True)
        def find(node):
            while parent[node]!=node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        ans = 0
        while distance:
            d, pi, pj = distance.pop()
            ppi = find(pi)
            ppj = find(pj)
            if ppi!=ppj:
                groups-=1
                if size[ppi]>size[ppj]:
                    parent[ppj]=ppi
                    size[ppi]+=size[ppj]
                    cost[ppi]+=cost[ppj]+d
                else:
                    parent[ppi]=ppj
                    size[ppj]+=size[ppi]
                    cost[ppj]+=cost[ppi]+d
                if groups==1:
                    ans = max(cost[ppi], cost[ppj])
                    break
        return ans
        