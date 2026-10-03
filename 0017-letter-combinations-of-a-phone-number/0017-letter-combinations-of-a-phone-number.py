class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        subset = []

        def solve(index):
            if index == len(digits):
                result.append("".join(subset))
                return 
            for ch in char_map[digits[index]]:
                subset.append(ch)
                solve(index+1)
                subset.pop()
        solve(0)
        return result