import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        ans = []
        tickets.sort(reverse=True)
        for f, d in tickets:
            graph[f].append(d)
        def dfs(node):
            while graph[node]:
                n = graph[node].pop()
                dfs(n)
            ans.append(node)
        dfs('JFK')
        ans.reverse()
        return ans