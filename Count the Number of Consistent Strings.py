class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = set(allowed)
        ans = 0
        for word in words:
            tmp = set(word)
            for k in tmp:
                if k not in cnt:
                    break
            else:
                ans += 1
        return ans
