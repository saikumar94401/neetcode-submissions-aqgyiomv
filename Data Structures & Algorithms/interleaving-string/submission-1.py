class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp={}

        def interleave(i,j,k):
    
            if k==len(s3) and i==len(s1) and j==len(s2):
                return True
            if k==len(s3):
                return False
            if i>=len(s1) and j>=len(s2):
                return False
            if str(i)+str(j)+str(k) in dp:
                return dp[str(i)+str(j)+str(k)]
            
            temp=False
            if  i<len(s1) and s1[i]==s3[k]:
                temp =temp or interleave(i+1,j,k+1)
            if j<len(s2) and s2[j]==s3[k]:
                temp=temp or interleave(i,j+1,k+1)
            sub_string=str(i)+str(j)+str(k)
            dp[sub_string]=temp
            return temp



        return interleave(0,0,0)


