class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s=0
        e=len(nums)-1
        while s<=e:
            m=s+(e-s)//2
            if nums[m]==target:
                return m
            if nums[s]<=nums[m]:
                if target>=nums[s] and target<nums[m]:
                    e=m-1
                else:
                    s=m+1
            else:
                if target>nums[m] and target<=nums[e]:
                    s=m+1
                else:
                    e=m-1
        return -1
