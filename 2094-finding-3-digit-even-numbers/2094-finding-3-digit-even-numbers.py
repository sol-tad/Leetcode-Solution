class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        even_numbers = set()
        
        for perm in permutations(digits, 3):
            number = perm[0] * 100 + perm[1] * 10 + perm[2]
            
            if perm[0] != 0 and perm[2] % 2 == 0:
                even_numbers.add(number)
        
        return sorted(even_numbers)
      
        