 
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        value = [0]
        s = 0 
        for i in range(1,len(heights)):
            if heights[i] > heights[i-1]:
                heappush(heap,-(heights[i]- heights[i-1]))
                s += heights[i] - heights[i-1]
            if s > bricks and ladders > 0:
                ladders -= 1
                s += heappop(heap)
            if s > bricks and ladders == 0:
                return i-1

        return len(heights)-1
