# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root==None:
            return None
        q=[root]
        
        while q:
            size = len(q)
            for i in range(size):
                child=q[0]
                temp=child.left
                child.left=child.right
                child.right=temp
                q.pop(0)
                if child.left:
                    q.append(child.left)
                if child.right:
                    q.append(child.right)
        return root 