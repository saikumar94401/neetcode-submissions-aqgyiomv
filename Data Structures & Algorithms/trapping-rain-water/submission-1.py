class Solution:
    def trap(self, height: List[int]) -> int:
        max_area=0
        left=0
        right=len(height)-1

        max_left=height[left]
        max_right=height[right]

        while left<right:
            
            if height[left]< height[right]:
                max_area+=min(max_left,max_right)-height[left]
                if height[left+1]>max_left:
                    max_left=height[left+1]
                left+=1
            else:
                max_area+=min(max_left,max_right)-height[right]
                if height[right-1]>max_right:
                    max_right=height[right-1]
                right-=1
        return max_area
