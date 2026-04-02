class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            ind=abs(i)-1
            if nums[ind]<0:
                return abs(i)
            nums[ind]*=-1
        return -1