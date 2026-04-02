class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=[nums[0]]
        s=[nums[-1]]
        for i in range(1,len(nums)):
            a=p[i-1]
            p.append(a*nums[i])
        print(p)
        for i in range(len(nums)-2,-1,-1):
            print(i)
            a=s[0]
            s.insert(0,a*nums[i])
        print(s)
        ans=[s[1]]
        for i in range(1,len(nums)-1):
            ans.append(s[i+1]*p[i-1])
        ans.append(p[-2])

        return ans