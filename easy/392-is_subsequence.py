class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0

        for i in range(len(t)):
            if len(s) > j and t[i] == s[j]:
                j += 1

        return j == len(s)
