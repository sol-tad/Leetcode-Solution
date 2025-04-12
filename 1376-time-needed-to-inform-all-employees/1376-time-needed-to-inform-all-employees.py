class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = defaultdict(list)
        for i in range(n):
            if manager[i]!=-1:
                tree[manager[i]].append(i)
        # print(tree)
        def dfs(emp):
            max_time=0
            for sub in tree[emp]:
                max_time = max(max_time, dfs(sub))
            return informTime[emp]+max_time
        return dfs(headID)