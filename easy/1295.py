from typing import List

class solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count


nums = [12,345,2,6,7896]

sol = solution()
resultado = sol.findNumbers(nums)

print(resultado)
