# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result=root.val
        def maxSum(node) :
            nonlocal result
            if node==None :
                return 0

            left=maxSum(node.left)
            right=maxSum(node.right)
            
            max_children=max(left+right,left,right)
            result=max(result,max_children+node.val,node.val)

            return max(node.val,max(left,right)+node.val)

        maxSum(root)
        return result


        
