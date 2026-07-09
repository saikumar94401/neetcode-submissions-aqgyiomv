class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp=[1]+nums[:]+[1]
        memo={}
        def burstBallons(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j-i>2:
                temp=0
                for k in range(i+1,j):
                    left=burstBallons(i,k)
                    right=burstBallons(k,j) 
                    now=dp[i]*dp[k]*dp[j]
                    temp=max(temp,left+right+now)
                memo[(i,j)]=temp
                return temp
            else:
                if j-i==1:
                    return 0
                else:
                    memo[(i,j)]=dp[i]*dp[i+1]*dp[j]
                    return memo[(i,j)]

        return burstBallons(0,len(dp)-1)
        