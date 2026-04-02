class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        for i in range(n):
            e=n-i-1
            if i==0:
                prefix[i]=nums[i]
                suffix[e]=nums[e]
            else:
                prefix[i]=prefix[i-1]*nums[i]
                suffix[e]=suffix[e+1]*nums[e]
        result=[]
        for i in range(n):
            if i==0:
                result.append(suffix[i+1])
            elif i==n-1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1]*suffix[i+1])
        return result

