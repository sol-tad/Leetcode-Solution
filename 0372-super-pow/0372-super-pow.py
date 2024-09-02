class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        result = ''.join(map(str, b))
        res=int(result)
        return int((a**res)%1337)
        