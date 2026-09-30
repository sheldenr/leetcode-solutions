class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest = nums[0]

        def absolute_value(num):
            if num < 0:
                return -1 * num
            else:
                return num

        for num in nums:
            if absolute_value(num) < absolute_value(closest) or (absolute_value(num) == absolute_value(closest) and num > closest):
                closest = num

        return closest
