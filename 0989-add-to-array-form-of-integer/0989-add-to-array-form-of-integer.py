import sys
sys.set_int_max_str_digits(10**6)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_str = ''.join(map(str, num))
        total_sum = int(num_str) + k
        return [int(digit) for digit in str(total_sum)]
