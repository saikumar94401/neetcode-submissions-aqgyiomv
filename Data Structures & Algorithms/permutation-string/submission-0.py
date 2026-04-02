class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        if n1>n2:
            return False
        s1_freq=[0]*26
        s2_freq=[0]*26
        for i in range(n1):
            s1_freq[ord(s1[i])-ord('a')]+=1
            s2_freq[ord(s2[i])-ord('a')]+=1
        for i in range(n1,n2):
            if s1_freq==s2_freq:
                return True
            start_index=i-n1
            s2_freq[ord(s2[i])-ord('a')]+=1
            s2_freq[ord(s2[start_index])-ord('a')]-=1
        return s1_freq==s2_freq