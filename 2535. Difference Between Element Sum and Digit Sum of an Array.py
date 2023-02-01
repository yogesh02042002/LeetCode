class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        res = []
        for i in nums:
            se = 0
            for digit in str(i):
                se += int(digit)
            res.append(se)
        r=sum(res)
        return s-r
