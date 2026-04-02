"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        f=head
        d={}
        while f:
            n=Node(f.val)
            d[f]=n
            f=f.next
        
        for original,copy in d.items():
            copy.next=d[original.next] if original.next else None
            copy.random=d[original.random] if original.random else None
        
        return d[head] if head in d else None