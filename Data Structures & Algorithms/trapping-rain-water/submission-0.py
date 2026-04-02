class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        ml,mr=[-1 for _ in range(len(height))],[-1 for _ in range(len(height))]
        ml[0]=height[0]
        mr[r]=height[r]
        water=0
        for i in range(1,len(height)):
            ml[i]=max(height[i],ml[i-1])
        
        for i in range(len(height)-2,-1,-1):
            mr[i]=max(height[i],mr[i+1])
        
        for i in range(len(height)):
            w=min(ml[i],mr[i])-height[i]
            water+= w if w>0 else 0

        return water
