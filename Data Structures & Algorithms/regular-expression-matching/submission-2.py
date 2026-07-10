class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def regEx(i,j):
            if i==len(s) and j==len(p):
                return True
            if i!=len(s) and j==len(p):
                return False
            temp=False
            if j+1<len(p) and p[j+1]== "*":
                if p[j]!=".":
                    c=p[j] 
                    temp =temp or regEx(i,j+2) # zero occurances
                    while i<len(s) and s[i]==c: # for same char occurances
                        i+=1
                        temp =temp or regEx(i,j+2)
                else:
                    for k in range(i,len(s)+1):
                        temp=temp or regEx(k,j+2)
            elif (j<len(p) and i<len(s)) and (p[j]=="." or p[j]==s[i]):
                temp=temp or regEx(i+1,j+1)
            
            return temp

        return regEx(0,0)