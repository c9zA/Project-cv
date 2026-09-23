class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        ans = 0
        seen = set()
        def dfs(node):
            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    dfs(n)
        for i in range(n):
            if i not in seen:
                seen.add(i)
                ans += 1
                dfs(i)
        return ans