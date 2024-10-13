class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)

        for _ in range(k):
            num_str = str(sum(int(digit) for digit in num_str))
        
        return int(num_str)
        