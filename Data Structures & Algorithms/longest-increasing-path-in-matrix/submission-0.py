class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        visited=[ [-1]*n for _ in range(m)]
        print(visited)

        def longPath(i,j):
            if i<0 or j<0 or i>=m or j>=n :
                return 0
            # top
            temp=0
            if i-1>=0 and matrix[i-1][j]>matrix[i][j]:
                if visited[i-1][j]!=-1:
                    temp=max(temp,1+visited[i-1][j])
                else:
                    temp=max(temp,1+longPath(i-1,j))
                
            # down
            if i+1<m and matrix[i+1][j]>matrix[i][j]:
                if visited[i+1][j]!=-1:
                    temp=max(temp,1+visited[i+1][j])
                else:
                    temp=max(temp,1+longPath(i+1,j))
            
            # right
            if j+1<n and matrix[i][j+1]>matrix[i][j]:
                if visited[i][j+1]!=-1:
                    temp=max(temp,1+visited[i][j+1])
                else:
                    temp=max(temp,1+longPath(i,j+1))

            # left
            if j-1>=0 and matrix[i][j-1]>matrix[i][j]:
                if visited[i][j-1]!=-1:
                    temp=max(temp,1+visited[i][j-1])
                else:
                    temp=max(temp,1+longPath(i,j-1))
            visited[i][j]=temp
        
            return temp

        for i in range(m):
            for j in range(n):
                if visited[i][j]==-1:
                    longPath(i,j)
        result=0

        print(visited)
        for i in range(m):
            for j in range(n):
                result=max(result,visited[i][j])
        return result+1
        




        