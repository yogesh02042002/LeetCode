class Solution:
    def sortSentence(self, s: str) -> str:
        words=s[::-1].split()
        words.sort()
        res=[word[1:][::-1] for word in words]
        return ' '.join(res)
