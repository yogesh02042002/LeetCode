class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        sq=int(sqrt(num))
        s=1
        for i in range(2,sq+1):
            if num%i==0:
                t=num//i
                s+=t+i
        if s==num:
            return True
        return False
