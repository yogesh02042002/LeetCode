class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t=''.join(sorted(list(t)))
        s=''.join(sorted(list(s)))
        if s==t:
            return True
        else:
            return False
