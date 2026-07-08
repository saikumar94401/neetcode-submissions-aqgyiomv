class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo={}
        def convertTo(i,j):

            if j==len(word2) and i==len(word1):
                return 0
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            if (i,j) in memo:
                return memo[(i,j)]

           
            if word1[i]==word2[j]:
                memo[(i,j)]=convertTo(i+1,j+1)
                return memo[(i,j)]
            
            insert=1+convertTo(i,j+1)
            replace=1+convertTo(i+1,j+1)
            delete=1+convertTo(i+1,j)
            memo[(i,j)]=min(insert,delete,replace)
            return memo[(i,j)]
        

        result=convertTo(0,0)
        print(result)
        return result