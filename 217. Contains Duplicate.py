class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=Counter(nums)
        for i ,j in s.items():
            if j>1:
                return True
