class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1

        while i<j:
            s=numbers[i]
            e=numbers[j]
            if s+e==target:
                break
            elif s+e<target:
                i+=1
            else:
                j-=1
            
        return [i+1,j+1]
