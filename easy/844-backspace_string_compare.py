class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack, t_stack = [], []

        for i in range(len(s)):
            if s[i] != "#":
                s_stack.append(s[i])
            elif s[i] == "#" and s_stack:
                s_stack.pop() 

        for i in range(len(t)):
            if t[i] != "#":
                t_stack.append(t[i])
            elif t[i] == "#" and t_stack:
                t_stack.pop()

        return s_stack == t_stack
