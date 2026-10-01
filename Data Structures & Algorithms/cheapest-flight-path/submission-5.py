class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        distance = [float('inf')]*n
        for f, t, p in flights:
            graph[f].append((t, p))
        pq = [(0, 0, src)]
        distance[src] = 0
        stops = [float('inf')]*n
        stops[src] = 0
        while pq:
            stop, dist, node = heapq.heappop(pq)
            stop += 1
            if stop<=k+1:
                for nei, d in graph[node]:
                    if stop==k+1:
                        if nei==dst and distance[dst]>dist+d:
                            distance[dst] = dist+d
                    else:
                        if distance[nei]>dist+d or stops[nei]>stop:
                            distance[nei]= min(distance[nei],dist+d)
                            stops[nei] = stop
                            heapq.heappush(pq, (stop, distance[nei], nei))
        return distance[dst] if distance[dst]!=float('inf') else -1