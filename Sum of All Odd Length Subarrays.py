class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n =len(arr)
        ans = 0
        for i in range(1, n+1, 2):
            for j in range(0, n-i+1):
                ans += sum(arr[j:j+i])
        return ans
