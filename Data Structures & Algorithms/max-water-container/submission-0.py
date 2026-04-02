class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        l,r=0,len(heights)-1
        while l<r:
            area=max(area,(r-l)*min(heights[l],heights[r]))
            if heights[l]<heights[r]:
                l+=1
            elif heights[r]<heights[l]:
                r-=1
            else:
                if heights[r-1]>heights[l+1]:
                    r-=1
                else:
                    l+=1
        return area