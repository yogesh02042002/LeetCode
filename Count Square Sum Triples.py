class Solution:
    def countTriples(self, n: int) -> int:
        result = 0
        arr = [i * i for i in range(1, n + 1)]
        s = set(arr)
        for i in range(n):
	        for j in range(i + 1, n):
		        if arr[i] + arr[j] in s:
			        result += 2
        return result
