class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        ans=0
        dr=[(1,0),(-1,0),(0,1),(0,-1)]
        def bfs(r,c):
            from collections import deque
            res=1
            q=deque()
            q.append((r,c))
            visit.add((r,c))
            
            while q:
                rr,cc=q.popleft()
                for d in dr:
                    r,c=rr+d[0],cc+d[1]
                    if (r>=0 and r<rows and c>=0 and c<cols and 
                        grid[r][c]==1 and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        res+=1
            return res
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    ans=max(ans,bfs(r,c))
        
        return ans

                