class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 0
        repeated_a = ""

        
        while len(repeated_a) < len(b) + len(a):  
            repeated_a += a
            count += 1
            if b in repeated_a:
                return count

        return -1
