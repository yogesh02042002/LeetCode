class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l,c=0,0
        for i in s:
            if i=='L':
                c+=1
            else:
                c-=1
            if c==0:
                l+=1 
        return l
        
