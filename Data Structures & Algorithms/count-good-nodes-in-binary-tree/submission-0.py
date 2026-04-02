# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def d(node,m):
            if not node:
                return 0
            r=1 if node.val>=m else 0
            m=max(m,node.val)
            r+=d(node.left,m)
            r+=d(node.right,m)

            return r
        return d(root,root.val)

