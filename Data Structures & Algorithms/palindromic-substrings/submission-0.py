class Solution:
    def countSubstrings(self, s: str) -> int:
        result=0
        def checkPalindrome(start,end):
            nonlocal result
            while start>=0 and end<len(s) and s[start]==s[end]:
                result+=1
                start-=1
                end+=1
            
        
        for i in range(len(s)):
            result+=1
            if i-1>=0 and i+1 <len(s):
                
                checkPalindrome(i-1,i+1)
                
            if i+1 <len(s):
                checkPalindrome(i,i+1)
        return result 