"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        if not node:
            return None

        new={}
        print(node.val)
        new[node] = Node(node.val)
        q=deque()
        q.append(node)

        while q:
            p=q.popleft()
            for child in p.neighbors:
                if child not in new:
                    new[child]=Node(child.val)
                    q.append(child)
                new[p].neighbors.append(new[child])
        return new[node]

