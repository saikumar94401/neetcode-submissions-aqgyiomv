class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        look_up=set(nums)
        max_count=0
        for i in range(len(nums)):
            if nums[i]-1 in look_up:
                continue
            count=0
            num=nums[i]
            while True:
                if num not in look_up:
                    break
                count+=1
                num+=1
            if count>max_count:
                max_count=count
        return max_count
