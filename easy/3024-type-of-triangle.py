class Solution:
    def triangleType(self, nums: List[int]) -> str:
        sidesSet = set()

        nums.sort()

        if nums[0] + nums[1] > nums[2]:
            for num in nums:
                sidesSet.add(num)

            if len(sidesSet) == 1:
                return "equilateral"
            elif len(sidesSet) == 2:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"
