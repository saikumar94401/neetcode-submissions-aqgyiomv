class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp=[[float("inf")]*(len(coins)+1) for _ in range(amount+1)]
        for i in range(len(dp[0])):
            dp[0][i]=0
        for total in range(1,len(dp)):
            for c in range(1,len(dp[0])):
                if total>=coins[c-1]  :
                    temp=dp[total-coins[c-1]][c]+1
                    dp[total][c]=min(dp[total][c-1],temp)                    
                else:
                    dp[total][c]=dp[total][c-1]
        
        
        if dp[amount][len(coins)]==float("inf") :
            return -1
        return dp[amount][len(coins)]