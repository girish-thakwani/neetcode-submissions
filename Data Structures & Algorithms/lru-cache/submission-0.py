class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.left=None
        self.right=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.left=Node(0,0)
        self.right=Node(0,0)

        self.left.right=self.right
        self.right.left=self.left

    def rem(self,node):
        print(node.key)
        prev=node.left
        nxt=node.right
        prev.right=nxt
        nxt.left=prev

    def ins(self,node):
        prev=self.right.left
        prev.right=node
        self.right.left=node
        node.right=self.right
        node.left=prev
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.rem(self.cache[key])
        self.ins(self.cache[key])
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.rem(self.cache[key])
        self.cache[key]=Node(key,value)
        self.ins(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.left.right
            self.rem(self.left.right)
            del self.cache[lru.key]
        
