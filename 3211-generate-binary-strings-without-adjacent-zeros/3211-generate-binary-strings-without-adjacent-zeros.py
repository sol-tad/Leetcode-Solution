class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def backtrack(path):
            if len(path)==n:
                res.append(path)
                return
            backtrack(path + '1')
            if not path or path[-1]!='0':
                backtrack(path+'0')

        backtrack("")
        return res
           