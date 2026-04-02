class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        ans=[l,r]
        while l<r:
            if target<(numbers[r]+numbers[l]):
                r-=1
            elif target>(numbers[r]+numbers[l]):
                l+=1
            elif target==(numbers[r]+numbers[l]):
                return [l+1,r+1]
        return ans