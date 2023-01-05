class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        a={')':'(', '}':'{', ']':'['}
        for i in s:
            if i in a.values():
                l.append(i)
            elif l and a[i]==l[-1]:
                l.pop()
            else:
                return False
        return l==[]
