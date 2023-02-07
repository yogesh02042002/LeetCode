class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = int(0.05*len(arr))
        m=(arr[n : len(arr) - n])
        return mean(m)
