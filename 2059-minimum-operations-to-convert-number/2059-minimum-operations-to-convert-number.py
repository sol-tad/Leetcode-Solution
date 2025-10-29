class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        queue = deque([(start, 0)])  
        visited = set([start])

        while queue:
            x, steps = queue.popleft()

            for num in nums:
                for next_x in (x + num, x - num, x ^ num):
                    if next_x == goal:
                        return steps + 1
                    if 0 <= next_x <= 1000 and next_x not in visited:
                        visited.add(next_x)
                        queue.append((next_x, steps + 1))

        return -1  
