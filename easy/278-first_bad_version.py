# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        check midpoint
        if midpoint is good check to the right
        if midpoint is bad check it and to the left
        return first bad
        """

        l, r = 1, n

        while l < r:
            mid = (l + (r - l) // 2)

            if isBadVersion(mid) == False:
                l = mid + 1

            else:
                r = mid

        return l
