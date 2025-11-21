class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] * 26

        for a, b in zip(s, t):
            diff = (ord(b) - ord(a)) % 26
            if diff != 0:
                freq[diff] += 1
        
        for diff in range(1, 26):
            max_move_needed = diff + 26 * (freq[diff] - 1)
            if max_move_needed > k:
                return False

        return True
