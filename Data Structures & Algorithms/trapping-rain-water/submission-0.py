class Solution:
    def trap(self, height: List[int]) -> int:
        max_right=[0]*len(height)
        i=len(height)-2
        max_right[i+1]=height[i+1]
        max_area=0
        while(i>=0):
            if height[i]>max_right[i+1]:
                max_right[i]=height[i]
            else:
                max_right[i]=max_right[i+1]
            i-=1
        max_left=height[0]
        for i in range(1,len(height)):
        
            if height[i]>max_left:
                max_left=height[i]
                continue
            max_area+=min(max_left,max_right[i])-height[i]
        return max_area