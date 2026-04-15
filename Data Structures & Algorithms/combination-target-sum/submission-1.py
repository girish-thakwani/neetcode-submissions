class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        sol=[]
        def backtrack(i,total,sol):
            if total==target:
                res.append(sol[:])
                return 

            for j in range(i,len(nums)):
                if total>target:
                    return
                sol.append(nums[j])
                backtrack(j,total+nums[j],sol)
                sol.pop()

        backtrack(0,0,sol)
        return res