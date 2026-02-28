class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [ 0 ] * n

        for index in range(1, n + 1):
            if index % 3 == 0 and index % 5 == 0:
                res[index - 1] = "FizzBuzz"
            elif index % 3 == 0:
                res[index - 1] = "Fizz"
            elif index % 5 == 0:
                res[index - 1] = "Buzz"
            else:
                res[index - 1] = str(index)

        return res
