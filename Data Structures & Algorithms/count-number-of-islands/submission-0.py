class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        rows,cols=len(grid),len(grid[0])
        ans=0
        visited=set()
        dr=[(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                rr,cc=q.popleft()
                for d in dr:
                    r,c=rr+d[0],cc+d[1]
                    if (r>=0 and r<rows and c>=0 and c<cols and grid[r][c]=='1'
                        and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    bfs(r,c)
                    ans+=1

        return ans