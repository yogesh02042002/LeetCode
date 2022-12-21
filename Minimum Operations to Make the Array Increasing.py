class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        p = 0
        for i in nums:
            if i <= p:
                p += 1
                c += p - i
            else:
                p = i
        return c
