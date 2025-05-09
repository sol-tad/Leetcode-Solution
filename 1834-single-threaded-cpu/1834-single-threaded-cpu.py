class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks=[(enq,proc,i)for i,(enq,proc)in enumerate(tasks)]
        tasks.sort()
        res,heap=[],[]
        time=i=0
        n=len(tasks)
        while i<n or heap:
            while i<n and tasks[i][0]<=time:
                enq,proc,idx=tasks[i]
                heapq.heappush(heap,(proc,idx))
                i+=1
            if heap:
                proc,idx=heapq.heappop(heap)
                time+=proc
                res.append(idx)
            else:
                time=tasks[i][0]
        return res