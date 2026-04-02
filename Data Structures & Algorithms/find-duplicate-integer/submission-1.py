class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0
        while True:
            fast=nums[nums[fast]]
            slow=nums[slow]            
            if fast==slow:
                break
        start=0
        while True :
            start=nums[start]
            slow=nums[slow]
            if start==slow:
                return start



                
            

        