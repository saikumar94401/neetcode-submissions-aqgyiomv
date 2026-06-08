class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0 for _ in range(n)]

        def houseRob(n):
            if n<0 :
                return 0
            if n==0:
                return nums[n]

            if dp[n]:
                return dp[n]

            dp[n]=  max(nums[n]+houseRob(n-2),houseRob(n-1))
            return dp[n]

        return houseRob(n-1)


