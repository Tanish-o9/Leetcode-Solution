class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        maxi = 0
        left = 0
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maxi = max(maxi, right - left + 1)
        return maxi