class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isNice(substr: str) -> bool:
            set_chars = set(substr)
            for ch in set_chars:
                if ch.swapcase() not in set_chars:
                    return False
            return True

        n = len(s)
        max_len = 0
        longest_nice_substr = ""

        for start in range(n):
            for end in range(start + 1, n + 1):
                substr = s[start:end]
                if isNice(substr) and len(substr) > max_len:
                    max_len = len(substr)
                    longest_nice_substr = substr

        return longest_nice_substr


