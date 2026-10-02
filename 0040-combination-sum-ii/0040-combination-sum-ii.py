class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        subset = []
        result = []

        def backtrack(index, total):
            if total == 0:
                result.append(subset.copy())
                return
            if total < 0:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > total:
                    break
                subset.append(candidates[i])
                backtrack(i+1, total - candidates[i])
                subset.pop()
        backtrack(0, target)
        return result
                
            