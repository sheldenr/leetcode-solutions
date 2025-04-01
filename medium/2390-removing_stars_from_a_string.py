class Solution:
    def removeStars(self, s: str) -> str:
	# Very easy solution, took me a couple seconds .-.
        char_stack = []

        for char in s:
            if char != "*":
                char_stack.append(char)
            elif char_stack:
                char_stack.pop()

        return "".join(char_stack)
