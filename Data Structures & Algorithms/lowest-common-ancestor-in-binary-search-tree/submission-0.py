# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lcu=root


        def traverse(root,p,q):
            if root.val >p.val and root.val<q.val:
                return root

            if root.val==p.val or root.val==q.val :
                return root
            
            if root.val>p.val and root.val>q.val:
                return traverse(root.left,p,q)

            
            return traverse(root.right,p,q)
        if p.val>q.val:
            p,q=q,p
        return traverse(root,p,q)
            
