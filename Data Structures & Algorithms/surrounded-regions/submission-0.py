class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])
        visited=[[False for _ in range(cols)]for _ in range(rows)]
        edge_Os=[]
        def count_edge_Os(edge_Os):
            for i in range(rows):
                if board[i][0]=="O" :
                    edge_Os.append((i,0))
                if board[i][cols-1]=="O":
                    edge_Os.append((i,cols-1))
            for j in range(cols-1):
                if board[0][j]=="O" :
                    edge_Os.append((0,j))
                if board[rows-1][j]=="O":
                    edge_Os.append((rows-1,j))
        count_edge_Os(edge_Os)

        
        def edge_connect_Os(r,c):
            
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            if  board[r][c]=="X" or visited[r][c]:
                return 
            visited[r][c]=True
            
            directions=[0,1,0,-1,0]
            for i in range(len(directions)-1):
                new_r=r+directions[i]
                new_c=c+directions[i+1]
                edge_connect_Os(new_r,new_c)

        # Track all 0's connected to the edge O's
        for r,c in edge_Os:
            edge_connect_Os(r,c)
        # update 0's which are not connected to edg O's or surround

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    if visited[r][c]==False:
                        board[r][c]="X"
    
                    


        


        