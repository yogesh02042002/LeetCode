class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)
        if len(l) == 0:
            l.append(-1)
            l.append(-1)
            return l
        else:
            l1 = []
            l1.append(min(l))
            l1.append(max(l))
            return l1
