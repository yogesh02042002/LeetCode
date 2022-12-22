class Solution:
    def countAsterisks(self, s: str) -> int:
        flag = False
        count = 0
        for i in s:
            if i == '|':
                flag = not flag
            elif i == '*' and flag == False:
                count += 1
        
        return count
