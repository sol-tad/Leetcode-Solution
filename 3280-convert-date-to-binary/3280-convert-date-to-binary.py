class Solution:
    def convertDateToBinary(self, date: str) -> str:

        year, month, day = date.split('-')
        
        year = int(year)
        month = int(month)
        day = int(day)
        
        year_binary = bin(year)[2:]  # Remove '0b' from the binary representation
        month_binary = bin(month)[2:]
        day_binary = bin(day)[2:]
        
        
        return year_binary + "-" + month_binary + "-" + day_binary
