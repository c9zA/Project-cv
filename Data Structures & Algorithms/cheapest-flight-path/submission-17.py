class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        distance = [float('inf')]*n
        for f, t, p in flights:
            graph[f].append((t, p))
        q = deque([(0,0,src)])
        distance[src] = 0
        while q:
            stop, dist, node = q.popleft()
            stop += 1
            if stop<=k+1:
                for nei, d in graph[node]:
                    if stop==k+1:
                        if nei==dst and distance[dst]>dist+d:
                            distance[dst] = dist+d
                    else:
                        if distance[nei]>dist+d:
                            distance[nei] = min(distance[nei],dist+d)
                            q.append((stop, distance[nei], nei))
        return distance[dst] if distance[dst]!=float('inf') else -1