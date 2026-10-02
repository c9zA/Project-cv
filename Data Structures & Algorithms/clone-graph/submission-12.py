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
        nodes[1] = Node(1)
        q = deque([(node)])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei.val not in nodes:
                    nodes[nei.val] = Node(nei.val)
                    q.append(nei)
                nodes[cur.val].neighbors.append(nodes[nei.val])
        return nodes[1]