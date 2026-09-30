class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        seen = set()
        n = len(points)
        for i in range(n):
            xi,yi = points[i]
            for j in range(i+1, n):
                xj,yj = points[j]
                graph[i].append((abs(xi-xj)+abs(yi-yj), j))
                graph[j].append((abs(xi-xj)+abs(yi-yj), i))
        pq = []
        ans = 0
        heapq.heappush(pq,(0,0))
        while pq:
            if len(seen)==n:
                break
            dist, node = heapq.heappop(pq)
            if node in seen:
                continue
            ans+=dist
            seen.add(node)
            for d, nei in graph[node]:
                #if nei not in seen:
                heapq.heappush(pq, (d,nei))
        return ans