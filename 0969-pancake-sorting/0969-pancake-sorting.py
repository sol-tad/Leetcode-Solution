class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(k):
            arr[:k] = arr[:k][::-1]  
    
        result = []
        n = len(arr)

        for size in range(n, 1, -1):  
            max_idx = arr.index(size)  

            if max_idx == size - 1:
                continue  

            if max_idx != 0:
                flip(max_idx + 1)  
                result.append(max_idx + 1)

            flip(size)  
            result.append(size)

        return result
        