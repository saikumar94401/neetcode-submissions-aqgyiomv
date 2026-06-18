class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
       
        def longestSequence(i,j):
            if i==len(nums):
                return 0
            if dp[i][j]:
                return dp[i][j]
            les=longestSequence(i+1,j) # do not include
            les2=0
            if j==-1 or nums[i]>nums[j]:
                les2=1+longestSequence(i+1,i)
            dp[i][j]=max(les,les2) 
            return dp[i][j]

        return longestSequence(0,-1)