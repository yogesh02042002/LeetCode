class Solution:
    def countBits(self, n: int) -> List[int]:
        l= [0]
        for num in range(1, n+1):
            count = 0
            while num:
                count += num & 1
                num = num >> 1
            l.append(count)
        return l
