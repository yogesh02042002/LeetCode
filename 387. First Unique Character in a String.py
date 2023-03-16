class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = set()
        for i in range(0, len(s)):
            if s[i] not in a and s.count(s[i]) == 1:
                return i
            elif s[i] not in a:
                a.add(s[i])
        return -1
