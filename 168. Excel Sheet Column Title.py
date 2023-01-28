class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = [chr(x) for x in range(65, 91)]
        s = ""
        x = columnNumber-1
        while x >= 0:
            s = letters[x % 26] + s
            x = (x // 26) - 1
        return s
