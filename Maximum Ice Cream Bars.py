class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sum=0
        c=0
        costs.sort()
        for i in costs:
            sum+=i
            if sum<=coins:
                c+=1
        return c
