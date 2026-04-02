class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters={}
        n=len(s)
        start=0
        longest_substr=0
        i=0
        while i<n:
            if s[i] not in letters:
                letters[s[i]]=i
            else:
                if letters[s[i]] >= start:
                    longest_substr=max(longest_substr,i-start)
                    start=letters[s[i]]+1
                letters[s[i]]=i
            i+=1
        longest_substr=max(longest_substr,i-start)
        return longest_substr

