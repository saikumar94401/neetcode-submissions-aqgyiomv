class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        look_up=set(nums)
        max_count=0
        for number in look_up:
            if number-1 in look_up:
                continue
            num=number
            while True:
                if num not in look_up:
                    break
                num+=1
            count=num-number
            if count>max_count:
                max_count=count
        return max_count