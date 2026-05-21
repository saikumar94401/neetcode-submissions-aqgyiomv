class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def islands(i,j):
            print(i,j)
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="0" or grid[i][j]=="2":
                return 
            grid[i][j]="2"
                
            islands(i,j-1)
            # right
            islands(i,j+1)
            # top
            islands(i-1,j)
            # down
            islands(i+1,j)

        no_of_islands=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                
                    islands(i,j)
                    no_of_islands+=1
        return no_of_islands
                



