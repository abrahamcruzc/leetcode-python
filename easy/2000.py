class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i: int = word.find(ch)
        
        if i == -1:
            return word

        return word[:i+1][::-1] + word[i+1:]

word: str = "abcd"
ch: str = 'c'

sol: Solution = Solution()
result: str = sol.reversePrefix(word, ch)

print(result)
