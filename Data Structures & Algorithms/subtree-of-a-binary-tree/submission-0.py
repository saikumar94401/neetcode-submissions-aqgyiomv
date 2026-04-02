# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def checkSubTree(root,subRoot) :
            if subRoot== None and root ==None:
                return True
            
            if  subRoot and  root and subRoot.val!=root.val:
                return False
            
            if subRoot==None or root==None:
                return False
            left=checkSubTree(root.left,subRoot.left)
            right=checkSubTree(root.right,subRoot.right)

            return left and right

        def traverse(root,subRoot) :
            if root==None:
                return False
            
            if root.val==subRoot.val :
                result=checkSubTree(root,subRoot)
                if result :
                    return True
                
            left=traverse(root.left,subRoot)
            right=traverse(root.right,subRoot)

            return left or right

        return traverse(root,subRoot)
    
