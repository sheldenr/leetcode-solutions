class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_list = set(nums)
        seen = set()
        largest_sequence = 0
        starting_indices = []

        # Gets starting indicies to check for sequences
        for i in range(len(nums)):
            if (nums[i] - 1) not in number_list and (nums[i] - 1) not in seen:
                seen.add(nums[i] - 1)
                starting_indices.append(i)
        
        # Looks at each starting index and determines the sequence in the number_list
        for index in starting_indices:
            sequence = 1
            next_in_sequence = nums[index] + 1
            
            while (next_in_sequence) in number_list:
                next_in_sequence += 1
                sequence += 1

            largest_sequence = max(largest_sequence, sequence)

        return largest_sequence


        
