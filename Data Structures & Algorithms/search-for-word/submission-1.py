class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def wordSearch(i,j,idx,valid):
            
            if idx== len(word):
                return True
            if i<0 or i==len(board) or j<0 or j==len(board[0]) or board[i][j]!=word[idx] or valid[i][j]==1:
                return False
            valid[i][j]=1
            # left
            left=wordSearch(i-1,j,idx+1,valid)
            # right
            right=wordSearch(i+1,j,idx+1,valid)
            # top
            top=wordSearch(i,j-1,idx+1,valid)
            # down
            bottom=wordSearch(i,j+1,idx+1,valid)
            valid[i][j]=0
            return left or right or top or bottom 





        valid = [[0 for j in range(len(board[0]))]for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                   isValid= wordSearch(i,j,0,valid)
                   print(isValid)
                   if isValid:
                        return True
        return False


