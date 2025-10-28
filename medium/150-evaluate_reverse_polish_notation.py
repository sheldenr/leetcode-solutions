class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        token_set = set(["/","*","+","-"])

        for token in tokens:
            if token in token_set:
                value_2 = stack.pop()
                value_1 = stack.pop()

                if token == "/":
                    stack.append(int(int(value_1) / int(value_2)))
                if token == "*":
                    stack.append(int(value_1) * int(value_2))
                if token == "+":
                    stack.append(int(value_1) + int(value_2))
                if token == "-":
                    stack.append(int(value_1) - int(value_2))
                
            else:
                stack.append(int(token))

        return stack[0]

