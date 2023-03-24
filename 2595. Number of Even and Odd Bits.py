class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even=0
        odd=0
        b=bin(n)[2:]
        for i,val in enumerate(b[::-1]):
            if i%2==0 and val=='1':
                even+=1
            elif val=='1':
                odd+=1
        return [even,odd]
        
