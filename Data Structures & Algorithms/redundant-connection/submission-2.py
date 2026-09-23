class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        seen = set()
        candidates = set()
        seen.add(1)
        def dfs(seen, node):
            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    graph[n].remove(node)
                    result = dfs(seen, n)
                    seen.remove(n)
                    if result!=-1:
                        candidates.add((node, n))
                        if result==node:
                            return -1
                        return result
                else:
                    candidates.add((node, n))
                    return n
            return -1
        dfs(seen, 1)
        print(candidates)
        for a,b in edges:
            if len(candidates)>1:
                candidates.discard((a,b))
                candidates.discard((b,a))
            elif (a,b) in candidates or (b,a) in candidates:
                    return [a,b]
