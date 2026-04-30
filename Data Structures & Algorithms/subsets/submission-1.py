class Solution:

         

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def find_subset(sub,nums,i):
            if i== len(nums):
                return ;
            sub.append(nums[i])
            result.append(sub.copy())
        
            find_subset(sub,nums,i+1)
            sub.pop()
            find_subset(sub,nums,i+1)


        find_subset([],nums,0)


        
        result.append([])
        unique_list = [list(x) for x in set(tuple(x) for x in result)]
        return unique_list

            
