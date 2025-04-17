class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        placeholder_arr, j = nums[:], len(nums) - k

        for i in range(len(nums)):
            j %= len(nums)

            nums[i] = placeholder_arr[j]

            j += 1

