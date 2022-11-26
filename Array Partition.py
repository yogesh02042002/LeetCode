class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s=sum(nums[::2])
        return s
