class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""

        prefix = strs[0]
        length = len(prefix)

        for s in strs:
            while prefix != s[0:length]:
                prefix = prefix[0:length-1]
                length -= 1

                if length == 0:
                    return ""

        return prefix