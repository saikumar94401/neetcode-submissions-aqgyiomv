class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp=[0 for _ in range(n+1)]
        first=second=1
        for i in range(2,n+1):
            temp=first+second
            first=second
            second=temp



        return second