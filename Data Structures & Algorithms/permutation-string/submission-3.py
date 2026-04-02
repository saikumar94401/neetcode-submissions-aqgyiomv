class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        if n1>n2:
            return False
        # store the frequency of every alphabet in the array in 0-26 representing 'a'-'z'
        s1_freq=[0]*26
        s2_freq=[0]*26
        matches=0
        # store the frequences intial array of length n1 in both the arrays
        for i in range(n1):
            s1_freq[ord(s1[i])-ord('a')]+=1
            s2_freq[ord(s2[i])-ord('a')]+=1
        # matches all the freqencies of s1 to s2
        for i in range(26):
            matches+=(1 if s1_freq[i]==s2_freq[i] else 0)

        for i in range(n1,n2):
            if matches==26:
                return True

            # add element to the frequency array
            new_char_index=ord(s2[i])-ord('a')
            s2_freq[new_char_index]+=1
            if s2_freq[new_char_index]==s1_freq[new_char_index]:
                matches+=1
            elif s1_freq[new_char_index]==s2_freq[new_char_index]-1:
                matches-=1


            # remove starting element in frequency array

            old_char_index=ord(s2[i-n1])-ord('a')
            s2_freq[old_char_index]-=1
            if s2_freq[old_char_index]==s1_freq[old_char_index]:
                matches+=1
            elif s1_freq[old_char_index]==s2_freq[old_char_index]+1:
                matches-=1

            # after performing adding and subtraction of characters in the array 
            # the length of the s2 ==s1 in every step 

        return matches==26