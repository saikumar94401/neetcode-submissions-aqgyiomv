class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def swap(i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        
        def permutation(idx):
            if idx==len(nums):
                result.append(nums.copy())
            
            for i in range(idx,len(nums)):
                swap(i,idx)
                permutation(idx+1)
                swap(i,idx)
        result=[]
        permutation(0)
        return result