class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def maxArea(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            grid[i][j]=0
            # top
            top=maxArea(i - 1, j)
            # down
            down=maxArea(i + 1, j)
            # left
            left=maxArea(i, j - 1)
            # right
            right=maxArea(i, j + 1)
            return top+down+left+right+1
        maxi_area=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 :
                    maxi=maxArea(i,j)
                    maxi_area=max(maxi_area,maxi)
        return maxi_area

