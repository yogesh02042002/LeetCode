class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        print(cnt)
        for i,j in cnt.items():
            if j >1:
                return i
