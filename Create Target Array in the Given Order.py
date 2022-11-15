class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        t=[]
        for i in range(len(index)):
            t.insert(index[i],nums[i])
        return t
            
