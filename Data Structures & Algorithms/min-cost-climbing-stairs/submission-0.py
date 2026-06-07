class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0  for _ in range(n+1)]
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(1, len(dp)):
            dp[i]=min(dp[i-1],dp[i-2])
            if i<n:
                dp[i]+=cost[i]
        
            
        print(dp)
        return dp[n]





