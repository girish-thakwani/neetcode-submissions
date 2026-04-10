class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        c=Counter(tasks)
        d=[]
        for key,value in c.items():
            d.append([-value,key])
        
        del c
        t=0
        heapq.heapify(d)
        q=deque()
        s=""
        while d or q:
            t+=1
            
            if d:

                x=heapq.heappop(d)
                x[0]+=1
                s+=x[1]+""
                if x[0]!=0:
                    q.append([x,t+n])
            if q and q[0][1]==t:
                heapq.heappush(d,q.popleft()[0])
        

        print(s)
        return t