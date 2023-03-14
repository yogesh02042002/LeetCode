class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        c=0
        primes = [2,3,5,7,11,13,17,19,23,29,31]
        for i in range(left, right+1):
            l = bin(i).count('1')
            if l in primes:
                c += 1           
        return c
