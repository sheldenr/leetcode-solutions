class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_bits = []
        output = 0

        while n != 0:
            reverse_bits.append(n & 1)
            n >>= 1

        print(reverse_bits)

        for index, bit in enumerate(reverse_bits):
            output += (bit * (2 ** (31 - index)))

        return output
