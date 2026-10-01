class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []
        def solve(index):
            if index == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[index])
            solve(index + 1)
            subset.pop()
            solve(index + 1)

        solve(0)
        return result