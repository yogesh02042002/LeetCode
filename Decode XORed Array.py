class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l=[first]
        for i in range(len(encoded)):
            l.append(l[i]^encoded[i])
        return l
        
