class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        maximum_consecutive_chars = 0
        max_count = 0
        
        CharCount = {"T": 0, "F":0 }
        left = right = 0

        while right < n:

            CharCount[answerKey[right]] += 1
            max_count = max(max_count, CharCount[answerKey[right]])

            if (right - left + 1) - max_count > k:
                CharCount[answerKey[left]] -= 1
                left += 1
            
            maximum_consecutive_chars = max(maximum_consecutive_chars, right - left + 1)
            right += 1

        return maximum_consecutive_chars