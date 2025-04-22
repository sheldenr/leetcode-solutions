class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Another really shitty solution im sorry .-.
        num = int(float(dividend) / float(divisor))

        if num > ((2 ** 31) - 1):
            return ((2 ** 31) - 1)
        else:
            return num
