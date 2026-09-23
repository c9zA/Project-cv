class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        ans = 0
        q = deque()
        seen = set()
        for node in range(n):
            if node not in seen:
                q.append(node)
                seen.add(node)
                ans +=1
                while q:
                    cur = q.popleft()
                    for n in graph[cur]:
                        if n in seen:
                            continue
                        if n not in seen:
                            q.append(n)
                            seen.add(n)
        return ans