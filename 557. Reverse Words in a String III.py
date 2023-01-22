class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(" ")
        a=[i[::-1]for i in l]
        n=" ".join(a)
        return n
