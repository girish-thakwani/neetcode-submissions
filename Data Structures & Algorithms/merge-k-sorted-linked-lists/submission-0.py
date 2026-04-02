# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq as hq
        from queue import PriorityQueue
        import itertools
        counter=itertools.count()
        dummy=ListNode()
        head=dummy

        pq=PriorityQueue()

        for ll in lists:
            temp=ll
            while temp:
                pq.put((temp.val,next(counter),temp))
                temp=temp.next
        while not pq.empty():
            item=pq.get()
            head.next=item[2]
            head=head.next

        return dummy.next      
        

        
        