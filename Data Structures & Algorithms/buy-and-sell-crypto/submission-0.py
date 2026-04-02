class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        p = 0 
        ll = len(prices)
        while r<ll:
            if prices[l]<prices[r]:
                pro=prices[r]-prices[l]
                p=max(pro,p)
                r+=1
            else:
                l=r
                r+=1
        return p