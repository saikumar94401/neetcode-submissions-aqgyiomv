class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result=0
        def targetSum(i,total):
            if i==len(nums):
                if target==total:
                    return 1
                else:
                    return 0
            minus=targetSum(i+1,total+nums[i])
            plus=targetSum(i+1,total-nums[i])
            return minus+plus

        return targetSum(0,0)