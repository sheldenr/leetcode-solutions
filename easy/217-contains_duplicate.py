class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Two line solution it seems
        # Because sets remove duplicates, if the length of the set of nums and nums are the same, there are no dupilcates.
        num_set = set(nums)
        return len(num_set) != len(nums)
