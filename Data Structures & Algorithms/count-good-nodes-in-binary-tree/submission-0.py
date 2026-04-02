# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        result=0
        def traverse(node,maxi) :
            nonlocal result
            if node==None:
                return 
            updated_maxi=maxi
            if node.val >=maxi:
                result+=1
                updated_maxi=node.val
            
            traverse(node.left,updated_maxi)
            traverse(node.right,updated_maxi)
        traverse(root,root.val)
        return result