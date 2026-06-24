class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result=0
        memo={}
        def targetSum(i,total):
            if i==len(nums):
                if target==total:
                    return 1
                else:
                    return 0
            if (i,total) in memo:
                return memo[(i,total)]
            
            minus=targetSum(i+1,total+nums[i])
            plus=targetSum(i+1,total-nums[i])
            memo[(i,total)]=minus+plus
            return minus+plus

        return targetSum(0,0)