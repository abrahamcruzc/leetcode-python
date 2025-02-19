class Solution:
    def scoreOfString(self, s: str) -> int:
        dif = [abs(ord(s[i-1]) - ord(s[i])) for i in range(1, len(s))]

        return sum(dif)


sol = Solution()

s = 'hello'
result = sol.scoreOfString(s)
print(result)
