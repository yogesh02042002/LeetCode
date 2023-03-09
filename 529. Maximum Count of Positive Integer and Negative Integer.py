class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=p=0
        for i in nums:
            if i==0:
                continue
            elif i>0:
                p+=1
            else:
                n+=1
        return max(n,p)
