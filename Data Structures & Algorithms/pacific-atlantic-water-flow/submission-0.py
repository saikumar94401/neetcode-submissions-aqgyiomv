class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific=set()
        atlantic=set()
        rows=len(heights)
        cols=len(heights[0])

        def dfs(r,c,visited):
            visited.add((r,c))
            directions=[0,1,0,-1,0]
            
            for i in range(len(directions)-1):
                row=r+directions[i]
                col=c+directions[i+1]

                if row<0 or col<0 or row>=rows or col>=cols:
                    continue

                if (row,col) in visited:
                    continue
                
                current_height=heights[r][c]
                neighbour_height=heights[row][col]

                if current_height > neighbour_height:
                    continue
                
                dfs(row,col,visited)



                





        for i in range(rows):

            # first column 
            dfs(i,0,pacific)
            # last column
            dfs(i,cols-1,atlantic)

        for j in range(cols):
            
            #first row
            dfs(0,j,pacific)
            # last row
            dfs(rows-1,j,atlantic)
        result=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result