class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def wordSearch(i,j,idx):
            
            if idx== len(word):
                return True
            if i<0 or i==len(board) or j<0 or j==len(board[0]) or board[i][j]!=word[idx] :
                return False
            temp=board[i][j]
            board[i][j]="#"
            # left
            found=wordSearch(i-1,j,idx+1) or wordSearch(i+1,j,idx+1) or wordSearch(i,j-1,idx+1) or wordSearch(i,j+1,idx+1)
            
            board[i][j]=temp
            return found





       
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                   isValid= wordSearch(i,j,0)
                   if isValid:
                        return True
        return False


