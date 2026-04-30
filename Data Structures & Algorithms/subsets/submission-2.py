class Solution:

         

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        sub=[]
        def find_subset(i):
            if i== len(nums):
                result.append(sub.copy())
                return
            sub.append(nums[i])

        
            find_subset(i+1)
            sub.pop()
            find_subset(i+1)


        find_subset(0)


        
        print(result)
       
        return result

            
