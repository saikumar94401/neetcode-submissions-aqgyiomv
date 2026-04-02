class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        r=len(matrix)
        c=len(matrix[0])
        j=r*c-1

        while i<=j:
            mid= i+(j-i)//2
            row=mid//c
            col=mid%c
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                i=mid+1
            else:
                j=mid-1
        
        return False