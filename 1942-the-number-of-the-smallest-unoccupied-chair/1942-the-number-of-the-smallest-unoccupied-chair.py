class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arrival=defaultdict(list)
        leave=defaultdict(list)
        chair=defaultdict(int)
        mins,maxs=float('inf'),0
        for i in range(len(times)):
            arrival[times[i][0]].append(i)
            leave[times[i][1]].append(i)
            mins=min(mins,times[i][0])
        # print(arrival)
        # print(leave)

        heap=list(range(len(times)))
        heapify(heap)
        targetarr=times[targetFriend][0]
        for i in range(mins,targetarr+1):
            for n in leave[i]:
                heappush(heap,chair[n])
                # del chair[n]
            # leave[i]=[]

            for n in arrival[i]:
                ch=heappop(heap)
                chair[n]=ch
            # print(char)   
        return chair[targetFriend]  

            


