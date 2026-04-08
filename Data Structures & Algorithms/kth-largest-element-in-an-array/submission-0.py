class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-i for i in nums]
        heapq.heapify(nums)
        ans=-100000
        while k:
            k-=1
            ans=heapq.heappop(nums)
        return -ans