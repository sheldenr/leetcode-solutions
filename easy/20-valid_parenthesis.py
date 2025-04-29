class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        opening_set = set(["(", "{", "["])
        closing_set = set([")", "}", "]"])

        for bracket in s:
            if not stack:
                stack.append(bracket)
            else:
                if bracket == ")" and stack[-1] == "(":
                    stack.pop()
                elif bracket == "]" and stack[-1] == "[":
                    stack.pop()
                elif bracket == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(bracket)

        return len(stack) == 0
