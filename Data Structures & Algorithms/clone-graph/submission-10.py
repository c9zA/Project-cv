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
        seen = set()
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if (cur.val, nei.val) in seen:
                    continue
                if nei.val not in nodes:
                    nodes[nei.val] = Node(nei.val)
                nodes[nei.val].neighbors.append(nodes[cur.val])
                nodes[cur.val].neighbors.append(nodes[nei.val])
                seen.add((cur.val, nei.val))
                seen.add((nei.val, cur.val))
                q.append(nei)
        return nodes[1]