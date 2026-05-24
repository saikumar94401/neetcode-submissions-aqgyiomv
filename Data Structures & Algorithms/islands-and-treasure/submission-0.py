class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows=len(grid)
        cols=len(grid[0])

        def treasureHunt(r,c,distance):
            
            if  grid[r][c]==-1:
                return 

            directions=[0,1,0,-1,0]

            for d in range(len(directions)-1):
                
                new_row=r+directions[d]
                new_col=c+directions[d+1]
                
                if new_row<0 or new_col<0 or new_row>=rows or new_col>=cols:
                    continue

                if grid[new_row][new_col]> distance:
                    grid[new_row][new_col]=distance

                    treasureHunt(new_row,new_col,distance+1)



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    treasureHunt(r,c,1)
