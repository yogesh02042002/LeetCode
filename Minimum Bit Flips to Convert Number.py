class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
    
        while(start > 0 or goal > 0):
            check1 = (start & 1)
            check2 = (goal & 1)
        
            if(check1 != check2):
                count += 1
         
            start>>=1
            goal>>=1
 
        return count
