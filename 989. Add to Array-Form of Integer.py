class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        s = int("".join(map(str, num)))
        res=s+k
        l=list(map(int,str(res)))
        return l
