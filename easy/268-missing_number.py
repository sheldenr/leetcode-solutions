class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Not the expected bit manipulation method I assume
        expected_set = set(range(len(nums) + 1))
        actual_set = set(nums)

        for num in expected_set:
            if num not in actual_set:
                return num
