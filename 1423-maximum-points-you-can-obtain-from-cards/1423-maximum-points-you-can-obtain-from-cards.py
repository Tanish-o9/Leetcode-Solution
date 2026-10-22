class Solution:
    def maxScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left_sum = 0
        right_sum = 0
        if n == k:
            return sum(nums)
        for i in range(k):
            left_sum += nums[i]
        maxi = left_sum
        right_ind = n - 1
        for i in range(k - 1, -1, -1):
            left_sum -= nums[i]
            right_sum += nums[right_ind]
            maxi = max(maxi, left_sum + right_sum)
            right_ind -= 1
        return maxi