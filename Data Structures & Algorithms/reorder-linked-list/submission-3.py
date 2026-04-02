# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        

        if head ==None or head.next ==None:
            return None
        fast=head
        slow=head
        before_slow=head

        while fast and fast.next:
            fast=fast.next.next
            before_slow=slow
            slow=slow.next
        
        if fast!=None:
            before_slow=before_slow.next
            slow=slow.next
        temp=slow
        
        
        prev=temp.next
        temp.next=None
        while  prev!=None:
            after=prev.next
            prev.next=temp
            temp=prev
            prev=after

        
        before_slow.next=None
        slow=temp
        

        second=slow
        first=head
        while first!=None and second!= None  :
           
            # store next nodes
            first_next=first.next
            second_next=second.next
            # connect the node
            first.next=second
            second.next=first_next
    
            first=first_next
            second=second_next
        
           
      
        
        
        

    
        


    

        




        
