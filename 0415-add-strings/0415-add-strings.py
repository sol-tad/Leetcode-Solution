class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        result = []
        carry = 0
        max_length = max(len(num1), len(num2))
        
        for i in range(max_length):
            digit1 = int(num1[i]) if i < len(num1) else 0
            digit2 = int(num2[i]) if i < len(num2) else 0
            total = digit1 + digit2 + carry
            result.append(str(total % 10))
            carry = total // 10
        
        if carry:
            result.append(str(carry))
        
        return ''.join(result[::-1])
        