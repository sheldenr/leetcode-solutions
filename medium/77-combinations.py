class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans, sol = [], []

        def backtrack(start):
            if len(sol) == k:
                ans.append(sol.copy())
                return

            for i in range(start, n + 1):
                sol.append(i)
                backtrack(i + 1)
                sol.pop()

        backtrack(1)
        return ans
