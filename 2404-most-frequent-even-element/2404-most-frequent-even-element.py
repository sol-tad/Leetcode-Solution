class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num % 2 == 0: 
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1

        if not freq:
            return -1

        most_frequent = -1
        max_count = 0

        for num in freq:
            if freq[num] > max_count or (freq[num] == max_count and num < most_frequent):
                most_frequent = num
                max_count = freq[num]

        return most_frequent
