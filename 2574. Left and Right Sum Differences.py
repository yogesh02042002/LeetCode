class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            l.append(abs(sum((nums[:i]))-(sum(nums[i+1:]))))
        return l
