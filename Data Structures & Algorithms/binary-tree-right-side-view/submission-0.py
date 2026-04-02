# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=[root]
        r=[]

        while q:
            l=len(q)
            r.append(q[-1].val)
            for i in range(l):
                ele=q[0]
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
                q.pop(0)

        return r

