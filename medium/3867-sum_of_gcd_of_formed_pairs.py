class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = nums[:]
        output = 0

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return abs(a)

        max_value_seen = nums[0]
      
        for i in range(len(nums)):
            max_value_seen = max(max_value_seen, nums[i])
            prefixGcd[i] = gcd(nums[i], max_value_seen)

        prefixGcd.sort()
        
        for i in range(len(nums) // 2):
            last = len(nums) - 1 - i

            output += gcd(prefixGcd[i], prefixGcd[last])

        return output
