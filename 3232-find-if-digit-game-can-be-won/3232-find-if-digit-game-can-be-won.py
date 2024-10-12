class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_sum = 0
        double_digit_sum = 0
        
        for num in nums:
            if 1 <= num <= 9:
                single_digit_sum += num
            elif 10 <= num <= 99:
                double_digit_sum += num
        
        if single_digit_sum!=double_digit_sum:

          return True
        return False

        