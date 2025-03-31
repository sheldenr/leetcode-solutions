# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1

        pick = n // 2

        while guess(pick) != 0:
            if guess(pick) == -1:
                pick -= 1
            else:
                pick += 1

        return pick



























