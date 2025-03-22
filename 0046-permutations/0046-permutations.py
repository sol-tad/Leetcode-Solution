class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
    
        def bk(path, remaining):
            if not remaining:
                result.append(path)
                return
            for i in range(len(remaining)):
                bk(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        bk([], nums)
        return result