class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[n]=True

        for i in range(n-1,-1,-1):
            for word in wordDict:
                
                wlen = len(word)
                
                if i+wlen-1<n:
                    
                    if word==s[i:i+wlen]:
                        if dp[i]==False:
                            dp[i]=dp[i+wlen]
        print(dp)
        return dp[0]
