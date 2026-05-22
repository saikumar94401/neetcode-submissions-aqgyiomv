class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        fresh_oranges=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append([i,j,0])
                if grid[i][j]==1:
                    fresh_oranges+=1
        
        max_count=0
        directions=[0,-1,0,1,0]
        while queue:
            r,c,count= queue.popleft()
            max_count=max(max_count,count)
            for i in range(len(directions)-1):
                row = r+directions[i]
                col= c+directions[i+1]

                if row <0 or col<0 or row >=len(grid) or col>=len(grid[0]) :
                    continue
                
                if grid[row][col]==1:
                    fresh_oranges-=1
                    grid[row][col]=2
                    queue.append([row,col,count+1])

        if fresh_oranges!=0:
            return -1
        return max_count


