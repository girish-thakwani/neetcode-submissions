# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q=[root]
        a=""
        while q:
            ele=q[0]
            q.pop(0)
            if not ele:
                a+="NULL "
            else:
                a+=str(ele.val)+" "
                q.append(ele.left)
                q.append(ele.right)
            
        a=a.strip()
        a=a.strip("NULL ")
        return a   
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=="":
            return None
        d=data.split(" ")
        def printq(l):
            r=""
            for i in range(len(l)):
                r+=l[i].val+" "
            print(r)
        print(d)
        n=TreeNode(int(d[0]))
        q=[n]
        i=1
        while q and i<len(d):
            ele=q[0]
            q.pop(0)
            
            if i<len(d) and d[i]!="NULL":
                ele.left=TreeNode(d[i])
                q.append(ele.left)
                
            i+=1

            if i<len(d) and d[i]!="NULL":
                ele.right=TreeNode(d[i])
                q.append(ele.right)
               
            i+=1
            
            printq(q)
        return n