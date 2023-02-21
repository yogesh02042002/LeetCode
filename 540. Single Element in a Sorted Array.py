class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s=Counter(nums)
        for i,j in s.items():
            if j==1:
                return i
