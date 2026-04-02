# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result=root.val
        def traverse(node,i,k) :
            nonlocal result
            if node==None :
                return i
            
            index= traverse(node.left,i,k)
            # print("Before increment index",index)
            index+=1
            # print(node.val,":",index)
            if index == k:
                # print("result",node.val)
                result=node.val
            else: 
                index= traverse(node.right,index,k)
            # print(index,"index when returning ",node.val)
            return index

        traverse(root,0,k)
        return result