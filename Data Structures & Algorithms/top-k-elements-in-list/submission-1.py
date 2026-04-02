from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d=Counter(nums)
        fr=[[] for i in range(len(nums)+1)]
        for key,value in d.items():
            
            fr[value].append(key)
        
        ans=[]
        for i in range(len(fr)-1,0,-1):
            for ele in fr[i]:
                ans.append(ele)
                if len(ans)>=k:
                    return ans
        return ans