class Solution:
    def isHappy(self, n: int) -> bool:
        # Split integer into separate numbers using type casting (str -> list)
        # Calculate next number in sequence
        sequence_set = set()

        while True:
            num_list = list(str(n))

            for num in num_list:
                n += (int(num) ** 2)

            if n == 1:
                return True
            else:
                if n in sequence_set:
                    return False
            
            sequence_set.add(n)

        return True

