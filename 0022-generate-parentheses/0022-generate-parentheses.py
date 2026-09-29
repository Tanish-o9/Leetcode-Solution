class Solution:
    def generateParenthesis(self, n):
        result = []
        brackets = [""] * (2 * n)
        def solve(ind, total):
            if ind >= len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return
            if total > len(brackets) - ind:
                return
            if total < 0:
                return
            brackets[ind] = "("
            solve(ind + 1, total + 1)
            brackets[ind] = ")"
            solve(ind + 1, total - 1)
        solve(0, 0)
        return result