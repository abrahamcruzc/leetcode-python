class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        i: int = 0
        for j in range(1, len(nums)):
            if nums[j]  != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

nums: list[int] = [0,0,1,1,1,2,2,3,3,4]

sol: Solution = Solution()
result: int = sol.removeDuplicates(nums)
print(result)
print(nums[:result])
