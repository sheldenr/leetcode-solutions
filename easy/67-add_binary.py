class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_dec = 0
        b_dec = 0
        output = ""

        for index, val in enumerate(a[::-1]):
            a_dec += (2 ** (index)) * int(val)

        for index, val in enumerate(b[::-1]):
            b_dec += (2 ** (index)) * int(val)

        final_dec = a_dec + b_dec

        return bin(final_dec)[2:]

    
