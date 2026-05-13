class Solution:

    result=[]
    


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        def combinations(start,target,sub):
            if  target==0:
                result.append(sub.copy())
                return 

            
            for i in range(start,len(candidates)):
                if target < candidates[i]:
                    break
                if i!=start and candidates[i]==candidates[i-1]:
                    continue # skip duplicates
                sub.append(candidates[i])
                combinations(i+1,target-candidates[i],sub)
                sub.pop()


        combinations(0,target,[])
        return result


