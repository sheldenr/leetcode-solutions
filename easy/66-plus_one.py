class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_string = ""
        output = []

        for num in digits:
            digit_string += str(num)

        new_num = str(int(digit_string) + 1)

        for num in new_num:
            output.append(int(num))

        return output
