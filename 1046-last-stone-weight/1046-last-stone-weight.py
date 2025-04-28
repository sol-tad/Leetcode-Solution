class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==0:
            return 0
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            if abs(first)>abs(second):
                heapq.heappush(stones,-1*(abs(first)-abs(second)))
        return abs(stones[0])