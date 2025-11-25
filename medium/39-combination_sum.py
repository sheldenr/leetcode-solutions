class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, candidate, total):
            if total == target:
                res.append(candidate.copy())
                return
            
            if index == len(candidates) or total > target:
                return

            candidate.append(candidates[index])
            dfs(index, candidate, total + candidates[index])

            candidate.pop()
            dfs(index + 1, candidate, total) # dont include candidate

        dfs(0, [], 0)
        return res

            
