class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=dict()

        i=0
        for i in range(len(nums)):
            if target-nums[i] in dic :
                break
            dic[nums[i]]=i;
        first=i
        print(dic)
        second=dic[target-nums[i]]
        return [second,first]
