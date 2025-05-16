class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters = [i for i, c in enumerate(s) if c.isalpha()]
        n = len(letters)
        res = []

        for mask in range(1 << n):
            chars = list(s)
            for j in range(n):
                idx = letters[j]
                if (mask >> j) & 1:
                    chars[idx] = chars[idx].upper()
                else:
                    chars[idx] = chars[idx].lower()
            res.append("".join(chars))

        return res
