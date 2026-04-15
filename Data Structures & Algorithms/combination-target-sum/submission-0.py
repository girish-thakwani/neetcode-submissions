class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        sol=[]
        def backtrack(i,total,sol):
            if i>=len(nums) or total>target:
                return
            if total==target:
                res.append(sol[:]) 
                return
            #include
            print(total)
            sol.append(nums[i])
            backtrack(i,total+nums[i],sol)

            #do not include
            sol.pop()
            backtrack(i+1,total,sol)

        backtrack(0,0,sol)
        return res