class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=0
        for i in ransomNote:
            if ransomNote.count(i)<=magazine.count(i):
                c+=1
        if c==len(ransomNote):
            return True
        else:
            return False
