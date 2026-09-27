import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(set)
        distance = [float('inf')]*n
        pq = []
        for u, v, t in times:
            if v!=k:
                graph[u].add((v,t))
        heapq.heappush(pq, (0,k))
        distance[k-1] = 0
        while pq:
            dist, node = heapq.heappop(pq)
            for nei, d in graph[node]:
                if dist+d<distance[nei-1]:
                    heapq.heappush(pq,(dist+d, nei))
                    distance[nei-1] = dist+d
        ans = max(distance)
        return ans if ans!=float('inf') else -1