class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # Initial solution, uses extra space
        # non_zeroes = []

        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         non_zeroes.append(nums[i])
        
        # for i in range(len(nums)):
        #     if i < len(non_zeroes):
        #         nums[i] = non_zeroes[i]
        #     else:
        #         nums[i] = 0




        # Two Pointer Approach (Optimal)

        j = 0 # next non-zero pointer

        for i in range(len(nums)):
            if nums[i] != 0: # if needs to be swapped
                nums[j], nums[i] = nums[i], nums[j] # swap
                j += 1 #increament pointer to next non-zero pointer pos


