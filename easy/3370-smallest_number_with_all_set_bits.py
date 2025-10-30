class Solution:
    def smallestNumber(self, n: int) -> int:
        digits = math.ceil(math.log(n + 1, 10) / math.log(2, 10))
        return (2 ** digits) - 1
