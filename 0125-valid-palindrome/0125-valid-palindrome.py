class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filtered_chars = [char for char in s if char.isalnum()]
        return filtered_chars == filtered_chars[::-1]
