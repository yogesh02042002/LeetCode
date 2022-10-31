class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        m=[]
        for i in range(len(nums)):
            m.append(nums[nums[i]])
        return m
