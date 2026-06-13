class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp=[[0]*(len(coins)+1) for _ in range(amount+1)]
        
        for total in range(1,len(dp)):
            for c in range(1,len(dp[0])):
                if total>=coins[c-1] and (dp[total-coins[c-1]][c]!=0 or total-coins[c-1]==0) :
                    
                    temp=dp[total-coins[c-1]][c]+1
                    if dp[total][c-1]!=0:
                        dp[total][c]=min(dp[total][c-1],temp)
                    else:
                        dp[total][c]=temp
                    
                else:
                    dp[total][c]=dp[total][c-1]
        
        
        if dp[amount][len(coins)]==0 and amount!=0:
            return -1
        return dp[amount][len(coins)]