class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result=[]
        def isPalindrome(s):
            n=len(s)
            for i in range(n//2):
                if s[i]!=s[n-i-1]:
                    return False
            return True
        
        def backtrack(start,sub):
            print(start)
            if start==len(s):
                result.append(sub.copy())
                return

            for i in range(start,len(s)):
                substr=s[start:i+1]
                if isPalindrome(substr):
                    sub.append(substr)
                    backtrack(i+1,sub)
                    sub.pop()

            


        backtrack(0,[])
        return result