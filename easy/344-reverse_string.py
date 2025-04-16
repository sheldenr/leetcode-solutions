class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Create a temp character to the latter value before its swapped
        # Swap first index and last index
        # Increment the indices

        temp_char = ""

        for i in range(len(s) // 2):
            temp_char = s[i]
            s[i] = s[-i - 1]
            s[-i - 1] = temp_char
