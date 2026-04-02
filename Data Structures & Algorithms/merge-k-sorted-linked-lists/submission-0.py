# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head=temp=ListNode()
        n=len(lists)
        min_index=-1 # locate the position of val in lists
        while True:
            for i in range(n):
                # compare value of first number is each list
                linked_list=lists[i]
                
                if linked_list!= None:
                    if min_index!=-1 :
                        if  linked_list.val< lists[min_index].val :
                            min_index=i
                    else:
                        min_index=i
        
            if min_index!=-1:
                node=ListNode(lists[min_index].val)
                temp.next=node
                temp=node
                lists[min_index]=lists[min_index].next
            else:
                break
            min_index=-1
        return head.next



            
