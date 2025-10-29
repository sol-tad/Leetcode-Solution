class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  
        def backtrack(start, target, path):
           
            if target == 0:
                res.append(list(path))
                return
            if target < 0:
                return

            prev = -1  
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
                prev = candidates[i]

        backtrack(0, target, [])
        return res
