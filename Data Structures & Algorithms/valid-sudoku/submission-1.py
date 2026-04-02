class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row of the board
        def check_row(row,col,board):
            num=board[row][col]
            for c in range(len(board[0])):
                if c==col:
                    continue
                if board[row][c]==num:
                    return False
            return True
        # check col of the board
        def check_col(row,col,board):
            num=board[row][col]
            for r in range(len(board)):
                if r==row:
                    continue
                if board[r][col]==num:
                    return False
            return True
        # check in the box
        def check_box(row,col,board):
            r=(row//3)*3
            c=(col//3)*3
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if i==row and j==col:
                        continue
                    if board[row][col]==board[i][j]:
                        return False
            return True


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!=".":
                    c1=check_row(i,j,board)
                    c2=check_col(i,j,board)
                    c3=check_box(i,j,board)
                    if not(c1 and c2 and c3):
                        return False
        return True