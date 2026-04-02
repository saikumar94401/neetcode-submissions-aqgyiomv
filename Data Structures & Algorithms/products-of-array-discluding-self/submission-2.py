class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
       
        result=[1]
        # prefix sum of the array
        for i in range(1,n):
            result.append(result[i-1]*nums[i-1])
        postfix=1
        for i in range(n-1,-1,-1):
            result[i]=postfix*result[i]
            postfix*=nums[i]
        
        return result

