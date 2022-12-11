class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=0
        a=s.strip()
        for i in range(len(a)):
            if a[i]==" ":
                l=0
            else:
                l+=1
        return l
