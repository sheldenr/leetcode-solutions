class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        place_index = 1

        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                nums[place_index] = nums[index]
                place_index += 1

        return place_index
