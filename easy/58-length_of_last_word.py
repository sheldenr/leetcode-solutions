class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Thank god for python
        return len(s.split()[-1])
