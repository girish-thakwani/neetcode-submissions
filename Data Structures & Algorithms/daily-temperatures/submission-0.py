class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        ans=[0 for _ in range(len(temperatures))]
        for i,temp in enumerate(temperatures):
            while s and s[-1][1]<temp:
                ans[s[-1][0]]=i-s[-1][0]
                s.pop()
            
            s.append([i,temp])
        return ans