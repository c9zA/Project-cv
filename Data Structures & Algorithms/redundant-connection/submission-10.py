class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # n = len(edges)
        # indegree = [0] * (n + 1)
        # adj = [[] for _ in range(n + 1)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        #     indegree[u] += 1
        #     indegree[v] += 1

        # q = deque()
        # for i in range(1, n + 1):
        #     if indegree[i] == 1:
        #         q.append(i)

        # while q:
        #     node = q.popleft()
        #     indegree[node] -= 1
        #     for nei in adj[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 1:
        #             q.append(nei)

        # for u, v in reversed(edges):
        #     if indegree[u] == 2==indegree[v]:
        #         return [u, v]
        # return []
        n = len(edges)
        size = [1]*(n+1)
        parent = [0]
        for i in range(1,n+1):
            parent.append(i)
        def find(node):
            while parent[node]!=node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        for a,b in edges:
            pa = find(a)
            pb = find(b)
            if pa==pb:
                return [a,b]
            if size[pa]>size[pb]:
                size[pa]+=size[pb]
                parent[pb]=pa
            else:
                size[pb]+=size[pa]
                parent[pa]=pb
