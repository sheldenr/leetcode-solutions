class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        # Create a counter hashmap with each of the distinct values being a key
        # If any of the values occur more than twice, the array cannot be split
        counter = {}

        for index, num in enumerate(nums):
            if counter.get(num):
                counter[num] += 1
            else:
                counter[num] = 1
        
        for key in counter:
            if counter[key] > 2:
                return False
        
        return True
        
