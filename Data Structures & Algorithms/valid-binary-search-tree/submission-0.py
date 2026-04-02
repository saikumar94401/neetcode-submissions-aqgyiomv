# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def validateBST(node,min,max) :
            if node==None :
                return True
            
            if node.val <= min or node.val >= max :
                return False
            
            left=validateBST(node.left,min,node.val)
            right=validateBST(node.right,node.val,max)
            return left and right


        return validateBST(root,float("-inf"),float("inf"))