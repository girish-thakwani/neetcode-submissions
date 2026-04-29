class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dd=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        
        f=0
        ans=0
        def bfs(l):
            q=deque(l)
            nonlocal f
            nonlocal ans
            while q and f>0:
                for _ in range(len(q)):
                    x=q.popleft()
                    for d in dd:
                        r=x[0]+d[0]
                        c=x[1]+d[1]
                        if r>=0 and c>=0 and r<rows and c<cols and grid[r][c]==1 and not visited[r][c]:
                            
                            visited[r][c]=1
                            q.append((r,c))
                            f-=1
                ans+=1

        rotten=[]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    f+=1        
                if grid[r][c]==2:
                    rotten.append([r,c])
        bfs(rotten)   
        return ans if f==0 else -1