class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        sentence = s.split()
        num = float('-inf')  
        
        for word in sentence:
            if word.isdigit():
                currNum = int(word)
                if currNum <= num:  
                    return False
                num = currNum  
                
        return True
