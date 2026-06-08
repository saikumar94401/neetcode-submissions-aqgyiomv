class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        first=nums[0]
        second=max(nums[0],nums[1])

        for i in range(2,n):
            temp=max(second,first+nums[i])
            first=second
            second=temp
        return second
