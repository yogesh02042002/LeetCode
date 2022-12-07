class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l=[]
        for i in range(len(heights)):
            l.append([heights[i],names[i]])
        l.sort(reverse=True)
        s=[]
        for i in l:
            s.append(i[1])
        return s
