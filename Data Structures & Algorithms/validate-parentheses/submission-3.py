class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack=deque()
        d={')':'(',']':'[','}':'{'}
        for i in s:
            if i in d:
                if len(stack) and stack[-1]==d[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if len(stack)==0 else False 