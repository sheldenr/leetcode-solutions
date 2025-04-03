class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        forward_stack, backward_stack = [], []

        for char in x_string:
            forward_stack.append(char)

        for char in x_string[::-1]:
            backward_stack.append(char)

        return forward_stack == backward_stack
