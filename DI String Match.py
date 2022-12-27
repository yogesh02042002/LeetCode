class Solution:
    def diStringMatch(self, s: str) -> List[int]:
      
        left = right = 0
        res = [0]
        for i in s:
            if i == "I":
                right += 1
                res.append(right)
            else:
                left -= 1
                res.append(left)
        return [i - left for i in res]
