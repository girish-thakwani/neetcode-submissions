class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(p):
            if len(p)==len(nums):
                res.append(p[:])
                return

            for num in nums:
                if num in p:
                    continue
                
                p.append(num)
                print(p)
                backtrack(p)
                p.pop()
        backtrack([])
        return res