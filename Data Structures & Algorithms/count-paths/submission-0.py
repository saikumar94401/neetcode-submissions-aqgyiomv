class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]


        def unique(i,j):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if dp[i][j]:
                return dp[i][j]
            # move left
            left=unique(i,j+1)
            # move down
            right=unique(i+1,j)
            
            dp[i][j]=left+right
            return left+right

        return unique(0,0)
        