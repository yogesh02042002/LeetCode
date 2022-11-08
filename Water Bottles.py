class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        r=numBottles*numExchange-1
        return r//(numExchange-1)
