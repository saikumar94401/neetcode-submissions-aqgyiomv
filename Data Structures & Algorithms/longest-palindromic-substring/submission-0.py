class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def checkPalindrome(start,end):
            while start>=0 and end<len(s) and s[start]==s[end]:
                start-=1
                end+=1
            return s[start+1:end]
        result=s[0]
        for i in range(len(s)):
            if i-1>=0 and i+1 <len(s):
                palindrome=checkPalindrome(i-1,i+1)
                if len(palindrome)>len(result):
                    result=palindrome
                
            if i+1 <len(s):
                palindrome=checkPalindrome(i,i+1)
                if len(palindrome)> len(result):
                    result=palindrome
        return result