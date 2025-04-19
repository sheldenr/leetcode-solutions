class Solution:
    def reverse(self, x: int) -> int:
        # Very scuffsed solution
        final_int = []
        unparsed_int_string = str(x)

        if unparsed_int_string[0] == "-":
            final_int.append("-")

        num_seen = False

        for c in unparsed_int_string[::-1]:
            num_seen = c.isalnum()
            if c == "0" and not num_seen:
                break
            elif c == "-":
                break
            else:
                final_int.append(c)
            
        final_string = "".join(final_int)
        number = int(final_string)
        
        if number > 2147483647 or number < -2147483647:
            return 0
        else:
            return number

