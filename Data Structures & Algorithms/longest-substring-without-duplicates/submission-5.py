class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters={}
        n=len(s)
        start=0
        longest_substr=0
        i=0
        while i<n:
            prev=start
            if s[i]  in letters and letters[s[i]] >= start:
                prev=start    
                start=letters[s[i]]+1
                

            letters[s[i]]=i
            longest_substr=max(longest_substr,i-prev)
            i+=1
        longest_substr=max(longest_substr,i-start)
        return longest_substr

