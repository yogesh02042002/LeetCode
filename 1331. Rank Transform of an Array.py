class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        l=[]
        arr1 = sorted(list(set(arr)))
        for i in range(len(arr1)):
            d[arr1[i]] = i+1
        for i in arr:
            l.append(d[i])
        return l
        
