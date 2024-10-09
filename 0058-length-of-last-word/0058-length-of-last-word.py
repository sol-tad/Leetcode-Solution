class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed=s.strip()
        s_list=trimmed.split()

        if s_list:
            return len(s_list[-1])
        else:
            return -1

        