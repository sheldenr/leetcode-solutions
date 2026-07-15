class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_digits = len(str(low))
        high_digits = len(str(high))

        sequential_digit_string = "123456789"
        output = []

        for curr_digits in range(low_digits, high_digits + 1):

            for i in range(10 - curr_digits):
                value = int(sequential_digit_string[i : i + curr_digits])

                if value >= low and value <= high:
                    output.append(value)

        return output
