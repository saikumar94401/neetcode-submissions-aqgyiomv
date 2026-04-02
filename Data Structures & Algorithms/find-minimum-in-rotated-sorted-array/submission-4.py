class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=max(nums)
        s=0
        e=len(nums)-1
        while s<e:
            mid=s+(e-s)//2
            if nums[mid]<nums[e]:
                e=mid
            else:
                s=mid+1
        return nums[s]
