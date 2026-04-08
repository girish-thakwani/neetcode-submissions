class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d=[((abs((points[i][0]**2)+(points[i][1])**2))**0.5,[points[i][0],points[i][1]]) for i in range(len(points))]
        heapq.heapify(d)
        ans=[]
        while k:
            k-=1
            x=heapq.heappop(d)
            ans.append(x[1])
        return ans