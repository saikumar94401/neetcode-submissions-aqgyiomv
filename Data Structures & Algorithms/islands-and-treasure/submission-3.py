class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])


        def bfs(queue):
            

            while queue:
                r,c,distance=queue.popleft()
                distance+=1
                directions=[0,1,0,-1,0]
                for d in range(len(directions)-1):
                    new_row=r+directions[d]
                    new_col=c+directions[d+1]

                    if new_row<0 or new_col<0 or new_row>=rows or new_col>=cols:
                        continue
                    if grid[new_row][new_col]==0 or grid[new_row][new_col]==-1:
                        continue
                    
                    if grid[new_row][new_col]>distance:
                        grid[new_row][new_col]=distance
                        queue.append((new_row,new_col,distance))
        queue=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    queue.append((r,c,0))
        bfs(queue)