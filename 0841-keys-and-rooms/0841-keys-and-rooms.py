class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
            n=len(rooms)
            visited=set()
            queue=deque([0]) 

            while queue:
                current=queue.popleft()
                if current in visited:
                    continue
                visited.add(current)
                for key in rooms[current]:
                    if key not in visited:
                        queue.append(key)

            return len(visited)==n