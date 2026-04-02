# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que=deque()
        if not root:
            return []
        result=[]
        que.append(root)
        while que :
            n=len(que)
            for i in range(n):
                node=que.popleft()
                if i==n-1:
                    result.append(node.val)
                if  node.left:
                    que.append(node.left)
                if  node.right:
                    que.append(node.right)
        return result
                
