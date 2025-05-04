class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        prereq_sets = [set() for _ in range(numCourses)]


        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:

            curr = queue.popleft()
            for neighbor in graph[curr]:

                prereq_sets[neighbor].add(curr)
                prereq_sets[neighbor].update(prereq_sets[curr])
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        result = []
        for u, v in queries:
            result.append(u in prereq_sets[v])

        return result