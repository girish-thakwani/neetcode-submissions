from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1={}
        l=[]
        for s in strs:
            a=tuple(sorted(Counter(s).items()))
            if a not in d1:
                d1[a]=[s]
            else: 
                d1[a].append(s)
        ans=[]
        for key,value in d1.items():
            ans.append(value)
        return ans