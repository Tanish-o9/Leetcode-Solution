class Solution:
    def jump(self, nums: list[int]) -> int:
        jump = 0
        left = 0
        right = 0
        while right < len(nums) - 1:
            farest = 0
            for i in range(left, right+1):
                farest = max(farest, i + nums[i])
            left = right + 1
            right = farest
            jump += 1
        return jump