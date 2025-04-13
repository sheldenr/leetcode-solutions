class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initial Solution Idea
        # Get the frequency of each number in a hashmap
        # Key can be the integer and the values can be the frequency 
        # Sort all of these in a bucket with bucket[i] being the numbers that had that freq
        # Scan from end of bucket to start

        freq = {}
        bucket = [None] * len(nums) 
        output = []

        for num in nums:
            if freq.get(num) is not None:
                freq[num] += 1
            else:
                freq[num] = 1

        for key, value in freq.items():
            if bucket[value] is not None:
                bucket[value].append(key)
            else:
                bucket[value] = [key]

        for i in range(len(bucket) - 1):
            pass
            # go through and get the elements from next k elements from bucket



