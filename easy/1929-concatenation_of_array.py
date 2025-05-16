class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = nums[:]

        for num in nums:
            output.append(num)

        return output


