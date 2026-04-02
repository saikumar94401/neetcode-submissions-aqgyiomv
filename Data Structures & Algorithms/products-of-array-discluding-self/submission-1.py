class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*(n+1)
        n=len(nums)
        prefix=[1]*(n+1)
        suffix=[1]*(n+1)
        for i in range(1,n+1):
            e=n-i
            prefix[i]=prefix[i-1]*nums[i-1]
            suffix[i]=suffix[i-1]*nums[e]
        result=[]
        for i in range(1,n+1):
           
            result.append(prefix[i-1]*suffix[n-i])
        return result

