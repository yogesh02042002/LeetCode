class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        l=Counter(tasks)
        c=0
        for i in l.values():
            if i==1:
                return -1
            c+=ceil(i/3)
        return c
