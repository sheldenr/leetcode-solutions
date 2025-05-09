class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num_sum = 0

            for num in list(str(num)):
                num_sum += int(num)
            
            num = num_sum

        return num
