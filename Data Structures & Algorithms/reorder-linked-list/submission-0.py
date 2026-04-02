# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def printlist(newhead):
            s=""
            while newhead:
                s+=str(newhead.val)+"->"
                newhead=newhead.next
            print(s)
        chead=head
        count=0        
        while chead:
            count+=1
            chead=chead.next
        halfhead=head
        for i in range(count//2):
            halfhead=halfhead.next
        printlist(head)
        prev,curr = None,halfhead
        
        while curr:
            nxt = curr.next
            curr.next=prev
            prev=curr
            curr = nxt
        printlist(prev)
        dummy=ListNode()
        node=dummy
        c=0
        lhead=head
        printlist(lhead)
        while lhead and prev:
            if c%2==0:
                node.next=lhead
                lhead=lhead.next
            else:
                node.next=prev
                prev=prev.next
            node=node.next
            c+=1
        head=dummy.next
        