# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head= ListNode(0)
        temp=head
        while list1 !=None and list2 !=None:
            newNode= ListNode()
            if list1.val<=list2.val:
                newNode.val=list1.val
                list1=list1.next
            else:
                newNode.val=list2.val
                list2=list2.next
            temp.next=newNode
            temp=newNode
        
        while list1 !=None:
            newNode= ListNode(list1.val)
            temp.next=newNode
            temp=newNode
            list1=list1.next
        
        while list2 !=None:
            newNode=ListNode(list2.val)
            temp.next=newNode
            temp=newNode
            list2=list2.next
        return head.next
        
            