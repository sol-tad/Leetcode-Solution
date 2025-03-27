class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def carsrepair(time):
            car=0
            for r in ranks:
                car+=int(sqrt(time/r))
            return car>=cars
        low,high=1,ranks[0]*cars*cars
        res=-1
        while low<=high:
            mid=(low+high)//2
            if carsrepair(mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res

