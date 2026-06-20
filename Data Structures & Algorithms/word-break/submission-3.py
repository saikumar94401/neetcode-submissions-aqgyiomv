class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={len(s):True}
        def dfs(itr):
            if itr in memo:
                return memo[itr]
            if itr==len(s) :
                return True
            
            temp=False
            for i in range(itr,len(s)):
                substring=s[itr:i+1]
                if substring in wordDict:

                    temp=temp or dfs(i+1)
            memo[itr]=temp
            return temp
        return dfs(0)