class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        snum = ''.join(map(str, digits))
        num = int(snum) + 1
        snum = str(num)
        return [int(s) for s in snum]