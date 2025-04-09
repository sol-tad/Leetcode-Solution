class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming=defaultdict(int)
        outgoing=defaultdict(int)

        for start,des in trust:
            outgoing[start]+=1
            incoming[des]+=1
        print(incoming,outgoing)
        for p in range(1,n+1):
            if incoming[p]==n-1 and outgoing[p]==0:
                return p
        return -1