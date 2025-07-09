class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])

            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack()
                    path.pop()

        backtrack()
        return res
