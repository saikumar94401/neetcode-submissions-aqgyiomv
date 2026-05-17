class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]


        def subsets(itr,sub):
            result.append(sub.copy())
                    

            for i in range(itr,len(nums)):
                if i>itr and nums[i]==nums[i-1]:
                    continue
                sub.append(nums[i])
                subsets(i+1,sub)
                sub.pop()



        subsets(0,[])
        return result
