class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for start_index in range(len(s) - 1):
            score += abs(ord(s[start_index]) - ord(s[start_index + 1]))

        return score
