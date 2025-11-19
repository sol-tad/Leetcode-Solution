class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        idxs = []*(n**2)
        val = 1
        values = defaultdict(int)
        flag = True
        for i in range(n-1,-1,-1):
            if flag:
                for j in range(n):
                    if board[i][j] != -1:
                        values[val] = board[i][j] 
                    val +=1
                flag = False
            else:
                for j in range(n-1,-1,-1):
                    if board[i][j] != -1:
                        values[val]= board[i][j]
                    val +=1
                flag = True
        print(board)
        graph = defaultdict(list)
        for i in range(n**2 + 1):
            for j in range(i + 1, min(i + 7,((n ** 2) + 1))):
                val = values[j] if values[j] else j
                graph[i].append(val)
        queue = deque([1])
        visited = set()
        level = 1
        while queue:
            for _ in range(len(queue)):
                x = queue.popleft()
                for neg in graph[x]:
                    if neg == n ** 2:
                        return level
                    if neg not in visited:
                        visited.add(neg)
                        queue.append(neg)
            level += 1
        return -1  





        