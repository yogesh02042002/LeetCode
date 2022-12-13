class Solution:
    def minimumSum(self, num: int) -> int:
        s = sorted(map(int, str(num)))
        num1 = s[0]*10 + s[2]; 
        num2 = s[1]*10 + s[3]
        num3 = s[0]*10 + s[3]; 
        num4 = s[1]*10 + s[2]
        return min(num1+num2, num3+num4)
