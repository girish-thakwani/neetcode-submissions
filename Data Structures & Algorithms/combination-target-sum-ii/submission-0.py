class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        sol=[]
        def backtrack(i,total,sol):
            if total==target:
                res.append(sol[:])
                return
            
            for j in range(i,len(candidates)):
                if total+candidates[j]>target:
                    continue
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                sol.append(candidates[j])
                backtrack(j+1,total+candidates[j],sol)
                sol.pop()
        backtrack(0,0,sol)
        return res