class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic=Counter(secret)-Counter(guess)
        c=0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                c+=1
        c2=len(secret)-sum(dic.values())-c
        return str(c)+"A"+str(c2)+"B"
