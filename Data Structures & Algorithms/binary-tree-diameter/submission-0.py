# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        r=0
        def d(root):
            nonlocal r
            if root==None:
                return 0

            left=d(root.left)
            right=d(root.right)

            r=max(r,left+right)
            print(r,left if left else 0, right if right else 0)
            return 1+max(left,right)

        d(root)
        return r
