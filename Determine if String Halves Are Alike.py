class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        c=0
        n=0
        s1=s[slice(0,len(s)//2)]
        s2=s[slice(len(s)//2,len(s))]
        for i in range(len(s1)):
            if s1[i] in l:
                c+=1
        for i in range(len(s2)):
            if s2[i] in l:
                n+=1
        if c==n:
            return True
        else:
            return False
