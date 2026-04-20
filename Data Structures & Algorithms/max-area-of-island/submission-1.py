class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows,cols=len(grid),len(grid[0])
        visited=set()

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited.add((r,c))
            cnt=1
            while q:
                row,col=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]

                for dx,dy in directions:
                    r=row+dx
                    c=col+dy
                    if (r in range(rows) and
                        c in range(cols) and 
                        grid[r][c]==1 and
                        (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))
                        cnt+=1
            return cnt          
                
        ans=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    ans=max(ans,bfs(r,c))
                    
                
        return ans