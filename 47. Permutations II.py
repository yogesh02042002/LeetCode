class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        s=permutations(nums)
        l=[]
        for i in s:
            if i not in l:
                l.append(i)
        return l
