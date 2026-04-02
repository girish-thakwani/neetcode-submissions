# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        r=root.val
        def d(node):
            nonlocal r
            if not node:
                return 0

            lm=max(d(node.left),0)
            rm=max(d(node.right),0)
            r=max(r,node.val+max(lm+rm,lm,rm))
            print(node.val,lm,rm,r)
            return node.val + max(lm,rm)
        d(root)
        return r