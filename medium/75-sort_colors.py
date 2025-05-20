class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        colors = [0] * 3

        for color in nums:
            colors[color] += 1

        index = 0

        for i in range(3):
            for j in range(colors[i]):
                nums[index] = i
                index += 1
        

    
            
