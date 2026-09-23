class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n==1:
            return True
        graph = collections.defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        q = deque()
        seen = set([edges[0][0]])
        q.append(edges[0][0])
        ct = 0
        while q:
            node = q.popleft()
            ct+=1
            for nod in graph[node]:
                if nod in seen:
                    return False
                graph[nod].remove(node)
                seen.add(nod)
                q.append(nod)
        return ct==n
