class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)

        def gcd(a, b):
            if b == 0:
                return a

            return gcd(b, a % b)

        return gcd(maximum, minimum)
