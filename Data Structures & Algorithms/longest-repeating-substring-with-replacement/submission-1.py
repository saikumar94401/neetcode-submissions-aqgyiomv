class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq=0
        result=0
        freq_dict={}
        start=0
        for i in range(len(s)):
            
            freq_dict[s[i]]=1+freq_dict.get(s[i],0)
            max_freq=max(max_freq,freq_dict[s[i]])
            
            while i-start+1-max_freq > k:
                freq_dict[s[start]]=freq_dict[s[start]]-1
                start+=1
            result=max(result,i-start+1)
        return result
