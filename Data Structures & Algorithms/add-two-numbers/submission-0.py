# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=temp=ListNode()
        carry=0
        while l1 or l2:
            
            add = 0
            if l1:
                add+=l1.val
                l1=l1.next
            if l2:
                add+=l2.val
                l2=l2.next
            add+=carry
            
            node=ListNode(add%10)
            temp.next=node
            temp=node
            
            carry=add//10
        if carry>0:
            node=ListNode(carry)
            temp.next=node
        return head.next


        

        