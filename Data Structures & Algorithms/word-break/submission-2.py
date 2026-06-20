class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={len(s):True}
        def dfs(itr):
            if itr in memo:
                return memo[itr]
            if itr==len(s) :
                return True
            
            
            for i in range(itr,len(s)):
                substring=s[itr:i+1]
                if substring in wordDict:

                    if dfs(i+1):
                        memo[i]=True
                        return True
            memo[itr]=False
            return False
        return dfs(0)