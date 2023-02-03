class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        l=[]
        for i in range(n+1):
            l.append(i)
        for j in l:
            if j not in nums:
                return j
