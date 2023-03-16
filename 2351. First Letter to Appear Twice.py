class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l=[]
        for i in range(len(s)):
            if s[i] in l:
                return s[i]
            else:
                l.append(s[i])
