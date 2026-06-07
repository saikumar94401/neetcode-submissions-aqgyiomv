class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)] 
        def recursiveStairs(n):
            if n==0 or n==1:
                return 1
            if dp[n]:
                return dp[n]
            dp[n]=recursiveStairs(n-1)+recursiveStairs(n-2)
            return dp[n]



        return recursiveStairs(n)