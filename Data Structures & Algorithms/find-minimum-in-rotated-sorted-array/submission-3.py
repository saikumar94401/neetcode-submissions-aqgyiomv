class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=max(nums)
        s=0
        e=len(nums)-1
        while s<=e:
            mid=s+(e-s)//2
            if nums[mid] > nums[s] and nums[mid] > nums[e]:
                s=mid+1
            elif nums[mid] < nums[e]:
                ans=min(ans,nums[mid])
                e=mid-1
            else:
                ans=min(ans,nums[mid])
                s=mid+1
        return ans
