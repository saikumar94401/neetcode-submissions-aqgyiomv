# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        start=head
        prev_itr=None
        while start:
            
            # start = starting node of every iteration
            itr=start
            # check if the linked list container k elmenents
            for _ in range(k-1):
                if itr:
                    itr=itr.next
            # if not do not change anything
            if itr==None:
                break
            # save node for next iteration
            after=itr.next

            prev=start
            cur=start.next

            while prev != itr:
                next_node = cur.next
                cur.next=prev
                prev=cur
                cur=next_node
            
            start.next=after

            if start==head:
                head=itr # update head for the first iteration
            else:
                prev_itr.next=itr
            
            prev_itr=start
            # update start for next iteration
            start = after
            

        return head

            
            





