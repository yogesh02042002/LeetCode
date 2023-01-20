class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        a = list(word).index(ch)
        l = (word[:a+1][::-1])
        x = list(word)            
        x[:a+1] = l
        return ''.join(x)
