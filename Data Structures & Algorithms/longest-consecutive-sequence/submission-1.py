class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        maxx=0
        for i in s:
            if (i-1) not in s:
                l=1
                while (l+i) in s:
                    l+=1
                maxx=max(maxx,l)
        return maxx    
