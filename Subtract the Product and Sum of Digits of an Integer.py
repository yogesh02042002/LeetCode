class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l=[]
        for i in str(n):
            l.append(int(i))
        s=sum(l)
        m=1
        for x in l:
            m*=x
        return m-s
            
