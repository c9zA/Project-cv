class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n==1:
            return True
        graph = collections.defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        ct = 0
        def dfs(seen, node):
            nonlocal ct
            ct+=1
            for n in graph[node]:
                if n in seen:
                    return False
                seen.add(n)
                graph[n].remove(node)
                if not dfs(seen, n):
                    return False
                seen.remove(n)
            #graph[node] = set()
            return True
        if not dfs(set([edges[0][0]]), edges[0][0]):
            return False
        return ct==n