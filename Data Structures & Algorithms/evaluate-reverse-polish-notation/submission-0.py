class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def operate(operand,nums):
            nums1,nums2=nums[0],nums[1]
            if operand == '+':
                return str(nums1+nums2)
            elif operand == '-':
                return str(nums1-nums2)
            elif operand == '*':
                return str(nums1*nums2)
            elif operand == '/':
                return str(int(nums1/nums2))

        stack=[]

        for i in tokens:
            if i in "+-*/":
                nums=[int(stack[-2]),int(stack[-1])]
                stack.pop()
                stack.pop()
                ans=operate(i,nums)
                stack.append(ans)
            else:
                stack.append(i)
        return int(stack[-1])