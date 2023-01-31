class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        nums1=list(map(int,str(num)))
        for i in nums1:
            if num%i==0:
                c+=1
        return c
