class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set, nums2_set = set(nums1), set(nums2)
        distinct1, distinct2 = [], []

        for val in nums1_set:
            if val not in nums2_set:
                distinct1.append(val)
        
        for val in nums2_set:
            if val not in nums1_set:
                distinct2.append(val)

        return [distinct1, distinct2]
     # I completed this solution in literally like 2 minutes, thats crazy 
