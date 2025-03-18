class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k=k-1
        arr=[i for i in range(1,n+1)]
        state=k
        def cicrle(index):
            nonlocal arr
            if len(arr)==1:
                return arr[0]      
            ind = (k+index)%len(arr)
            index=arr.index(arr[ind])
            arr.pop(ind)
            return  cicrle(ind)


        return cicrle(0)
       