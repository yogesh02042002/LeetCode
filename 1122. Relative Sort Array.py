class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l = []
        for i in arr2:
            while i in arr1:
                l.append(i)
                arr1.remove(i)
        return(l+sorted(arr1))
