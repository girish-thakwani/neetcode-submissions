class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss=set()
        l=0
        ans=0
        for i in range(len(s)):
            while s[i] in ss:
                ss.remove(s[l])
                l+=1
                
            ss.add(s[i])
            
            ans=max(len(ss),ans)
        return ans
            
