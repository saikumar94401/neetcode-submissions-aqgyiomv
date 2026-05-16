class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result,sub=[],[]
        def backtrackP(open,close):
            if close==n:
                result.append("".join(sub))
                return

            if open<n:
                sub.append("(")
                backtrackP(open+1,close)
                sub.pop()
            
            if open>close:
                sub.append(")")
                backtrackP(open,close+1)
                sub.pop()
        
        backtrackP(0,0)
        return result