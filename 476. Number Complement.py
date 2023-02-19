class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num).replace('0b',"")
        s=""
        for i in b:
            if i=="0":
                s+='1'
            else:
                s+='0'
        return int(s,2)
