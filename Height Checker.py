class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a = sorted(heights)
        b = []
        for i in range(len(heights)):
            if a[i] != heights[i]:
                b.append(i)
        return len(b)
