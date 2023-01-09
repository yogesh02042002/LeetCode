class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        var = '' 
        for element in digits: 
            var += str(element)
        s=int(var)+1
        l= list(map(int, str(s)))
        return l
