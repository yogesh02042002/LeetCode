class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        a=0
        s=["--X","X--"]
        for i in operations:
            if i in s:
                a-=1
            else:
                a+=1
        return a
