class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_container=0
        while i<j:
            if heights[i]<heights[j]:
                container=heights[i]*(j-i)
                i+=1
            else:
                container=heights[j]*(j-i)
                j-=1
            if container>max_container:
                max_container=container
        return max_container