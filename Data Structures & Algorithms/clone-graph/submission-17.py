"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = {}
        nodes[node] = Node(node.val)
        def dfs(n):
            for nei in n.neighbors:
                if nei not in nodes:
                    nodes[nei] = Node(nei.val)
                    dfs(nei)
                nodes[n].neighbors.append(nodes[nei])
        dfs(node)
        return nodes[node]