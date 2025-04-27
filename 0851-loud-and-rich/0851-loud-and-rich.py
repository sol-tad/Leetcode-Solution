
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n=len(quiet)
        graph=defaultdict(list)
        indegree=[0]*n

        for rich,poor in richer:
            graph[rich].append(poor)
            indegree[poor]+=1

        answer=list(range(n))

        queue=deque(i for i in range(n) if indegree[i]==0)

        while queue:
            person=queue.popleft()
            for neighbor in graph[person]:

                if quiet[answer[person]]<quiet[answer[neighbor]]:
                    answer[neighbor]=answer[person]
                    
                indegree[neighbor]-=1

                if indegree[neighbor]==0:
                    queue.append(neighbor)

        return answer
