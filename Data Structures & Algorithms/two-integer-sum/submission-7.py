from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1={}
        for i in range(len(nums)):
            if nums[i] not in d1:
                d1[nums[i]]=[i]
            else:
                d1[nums[i]].append(i)
        for i in range(len(nums)):
            if target-nums[i] in d1:
                if d1[target-nums[i]][0]==i:
                    if len(d1[target-nums[i]])>1:
                        return [i,d1[target-nums[i]][1]]
                    else:
                        continue
                return [i,d1[target-nums[i]][0]]
        return []