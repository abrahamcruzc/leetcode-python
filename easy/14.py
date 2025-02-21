from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        strs.sort()

        first: str = strs[0]
        last: str = strs[-1]
        
        i: int = 0
        
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]

strs: List[str] = ["flower","flow","flight"]

sol: Solution = Solution()
result: str = sol.longestCommonPrefix(strs)
print(result)
