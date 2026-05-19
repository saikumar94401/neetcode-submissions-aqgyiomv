class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        result=[]
        # abcd - len(s) = 4  start= 1,2,3,4

        for l in range(1,n+1):
            for start in range(n-l+1):
                end=start+l-1
                if s[start]==s[end] and ( start+1>end-1 or dp[start+1][end-1] ):
                    dp[start][end]=True
        def backtrack(itr,sub):
            if itr==n:
                result.append(sub.copy())
                return
            

            for i in range(itr,n):
                if dp[itr][i]:
                    sub.append(s[itr:i+1])
                    backtrack(i+1,sub)
                    sub.pop()
            

        backtrack(0,[])
        return result



            
            
            
            
       