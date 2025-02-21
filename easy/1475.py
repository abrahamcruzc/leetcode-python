from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack: List[int] = []
        
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                prices[index] -= prices[i]
            stack.append(i)
        
        return prices

prices: List[int] = [8,4,6,2,3]

sol: Solution = Solution()
result: List[int] = sol.finalPrices(prices)

print(result)
