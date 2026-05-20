class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        n=len(digits)
        result=[]
        
        if n<1:
            return result
        def letters(itr,n,sub):
            if itr==n:
                print(sub)
                result.append("".join(sub))
                return
            # print(phone[digits[itr]])
            for i in range(len(phone[digits[itr]])):
                    sub.append(phone[digits[itr]][i])
                    # print(phone[digits[itr]][i])
                    letters(itr+1,n,sub)
                    sub.pop()


        letters(0,n,[])
        return result