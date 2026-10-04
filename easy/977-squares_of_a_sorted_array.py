class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        index = len(nums)
        res = [0] * len(nums)

        def abs(val):
            if val >= 0:
                return val
            return (-1 * val)

        while l <= r:
            index -= 1

            if abs(nums[l]) >= abs(nums[r]):
                res[index] = (nums[l] ** 2)
                l += 1
            else:
                res[index] = (nums[r] ** 2)
                r -= 1

        return res
