class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        result=0
        decoder={"1":"A","2":"B","3":"C","4":"D","5":"E","6":"F","7":"G","8":"H","9":"I","10":"J","11":"K","12":"L","13":"M","14":"N","15":"O","16":"P","17":"Q","18":"R","19":"S","20":"T","21":"U","22":"V","23":"W","24":"X","25":"Y","26":"Z"}
        dp=[ 0 for _ in range(n)]
        result=0
        def decodeString(d):
            nonlocal result
            if d>=n:          # if parsing of string is completed
                return 1
            if dp[d]!=0:    # store the previous computation
                return dp[d]
            ans=0
            for i in range(2):
                if d+i+1<=n:
                    if s[d:d+i+1] in decoder:
                        ans+=decodeString(d+i+1)
            dp[d]=ans
            return ans
            
               
                

        decodeString(0)
        return dp[0]