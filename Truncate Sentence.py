class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=s.split()
        s=s[:k]
        s=' '.join(s)
        return s
