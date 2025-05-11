class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # This is a non optimal O(n^2) approach from as far as I can tell
        while val in nums:
            nums.remove(val)

        return len(nums)
        # what is this
