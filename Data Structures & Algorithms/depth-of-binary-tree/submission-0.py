# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0

        q=[root]
        d=0
        while q:
            n=len(q)
            for i in range(n):
                e=q[0]
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
                q.pop(0)
            d+=1
        return d