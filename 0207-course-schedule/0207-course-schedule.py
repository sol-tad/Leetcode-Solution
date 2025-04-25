class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        white = 0
        gray = 1
        black =2
        color = [0 for _ in range(numCourses)]
    
        def dfs(node):
            if color[node]==gray:
                return False
            if color[node]==black:
                return True
            color[node] = gray                          
            for ng in graph[node]:
                if color[ng] == 2:
                     continue 
                if not dfs(ng):
                    return False
            color[node] = black
            return True
        for i in range(numCourses):
            if color[i] == white:
                if not dfs(i):
                    return False 
          
        return True
