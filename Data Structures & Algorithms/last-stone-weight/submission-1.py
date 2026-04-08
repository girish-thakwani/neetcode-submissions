class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones=[-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones)>1:
            f=heapq.heappop(stones)
            s=heapq.heappop(stones)
            if s>f:
                heapq.heappush(stones,f-s)
        
        return abs(stones[0]) if stones else 0