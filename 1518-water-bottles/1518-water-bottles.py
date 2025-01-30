class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinksum=numBottles
        rem=numBottles%numExchange
        currdrink=numBottles//numExchange
        numBottles=currdrink+rem
        drinksum+=currdrink
        while numBottles>=numExchange:
            rem=numBottles%numExchange
            currdrink=numBottles//numExchange
            numBottles=currdrink+rem
            drinksum+=currdrink
        return drinksum


        