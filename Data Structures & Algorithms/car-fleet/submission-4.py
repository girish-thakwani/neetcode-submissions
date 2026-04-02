class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carl = [[position[i],speed[i]] for i in range(len(position))]
        carl.sort(key=lambda x:x[0])
        import math
        carld = [(target-carl[i][0])/carl[i][1] for i in range(len(speed))]
        stack =[]
        print(carl,carld)
        for i,time in enumerate(carld):
            while stack and stack[-1][1]<=time:
                stack.pop()
            stack.append([i,time])

        return len(stack)