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
        new_g={}
        q=[]
        q.append(node)
        new_g[node]=Node(node.val)
        while q:
            x=q.pop(0)
            for n in x.neighbors:
                if n not in new_g:
                    new_g[n]=Node(n.val)
                    q.append(n)
                new_g[x].neighbors.append(new_g[n])

        return new_g[node]