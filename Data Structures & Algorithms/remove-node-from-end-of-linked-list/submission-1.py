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

        temp=head
        node=dummy
        while temp!=None : 
            temp=temp.next
            if i>0:
                i-=1
            else:
                node=node.next
        node.next=node.next.next

        return dummy.next
        
        return head
