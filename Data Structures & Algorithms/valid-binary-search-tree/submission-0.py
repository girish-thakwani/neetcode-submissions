# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def d(l,node,r):
            if not node:
                return True
            if not ( node.val < r and node.val>l ):
                return False
            
            return d(l,node.left,node.val) and d(node.val,node.right,r)
        
        return d(-float("inf"),root,float("inf"))
        