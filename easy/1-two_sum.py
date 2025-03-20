class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## Brute Force Solution
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i , j]
        
        # Optimal Solution (O(n))
        seen = {} # Created a hashmap for O(1) time access of numbers
        
        for index, num in enumerate(nums):
            if seen.get(target-num) != None: # Evalute if difference is in current hashmap of seen numbers
                return [seen.get(target-num), index] # If number present, return indices of two numbers

            seen[num] = index # Add to list of seen numbers after viewing seen array to prevent cases where diff == current number ( i think? )
