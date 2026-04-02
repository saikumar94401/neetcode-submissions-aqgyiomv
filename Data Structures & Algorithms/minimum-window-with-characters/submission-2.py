class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len=len(s)
        t_len=len(t)

        result_len=float("inf")
        result=''


        if t_len> s_len:
            return ""

        # create dictionary to store frequencies for both the strings
        s_freq={}
        t_freq={}

        # store the frequencies of t in dictionary
        target=0
        for i in range(t_len):
            if t[i] in t_freq:
                t_freq[t[i]]+=1
            else:
                target+=1
                t_freq[t[i]]=1

        
        matches=0
        start=0
        for i in range(s_len):
            
            if s[i] in t_freq:
                s_freq[s[i]]=1+s_freq.get(s[i],0)
                if s_freq[s[i]]== t_freq[s[i]]:
                    matches+=1
            
            
            # if a valid substring is found
            while matches==target:

                if s[start] in t_freq:
                    if s_freq[s[start]] == t_freq[s[start]]:
                        matches-=1
                    s_freq[s[start]]-=1
                if i-start+1 <result_len:
                    result=s[start:i+1]
                    result_len=len(result)
                start+=1


                
        return result
                


            


        


        
        


        