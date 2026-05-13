class Solution:
    result=[]
    def combination(self,itr,cur,cur_candidates,target,candidates):
        if cur==target :
            self.result.append(cur_candidates.copy())
            return 
        if cur >target:
            return 
        
        for i in range(itr,len(candidates)):
            val=candidates[i]
            cur_candidates.append(val)
            self.combination(i,cur+val,cur_candidates,target,candidates)
            cur_candidates.pop()
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.result=[]
        self.combination(0,0,[],target,candidates)
        print(self.result)
        return self.result