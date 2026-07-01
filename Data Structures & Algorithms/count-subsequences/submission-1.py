class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[-1]*len(t) for _ in range(len(s))]
        def subsequence(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            temp=0
            if s[i]==t[j]:
                temp+=subsequence(i+1,j+1)
            
            temp+=subsequence(i+1,j)
            dp[i][j]=temp
            return temp
        return subsequence(0,0)