class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        n = len(g)
        m = len(s)

        g.sort()
        s.sort()

        left = 0
        right = 0
        count = 0

        while left<n and right<m:
            if g[left] <= s[right]:
                count += 1
                left += 1

            right += 1
        return count