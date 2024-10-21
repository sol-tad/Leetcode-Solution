class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        good = 0
        k=3
        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            if len(set(substring)) == k:  # check if all characters are unique
                good += 1
        return good
