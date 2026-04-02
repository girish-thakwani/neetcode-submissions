# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        r=True
        def d(root):
            nonlocal r
            if not root:
                return 0

            left=d(root.left)
            right=d(root.right)
            print(left if left else 0, right if right else 0)
            if abs(left-right)>1:
                r=False
            return 1+max(left,right)

        d(root)
        return r