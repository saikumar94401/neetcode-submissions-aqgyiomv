# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=n
        dummy=ListNode(-1)
        dummy.next=head

        prev=node=temp=dummy
        while temp!=None : 
            temp=temp.next
            if i>0:
                i-=1
            else:
                prev=node
                node=node.next
        prev.next=node.next

        return dummy.next
        
        return head
