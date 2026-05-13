class Solution:

    result=[]
    def combinations(self,itr,total,target,sub,candidates):
        if total>target:
            return
        if total== target:
            self.result.append(sub.copy())
        
        for i in range(itr,len(candidates)):
            if i!=itr and candidates[i]==candidates[i-1]:
                continue
            num=candidates[i]
            total+=num
            sub.append(num)
            self.combinations(i+1,total,target,sub,candidates)
            sub.pop()
            total-=num


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.result=[]
        self.combinations(0,0,target,[],candidates)
        return self.result


