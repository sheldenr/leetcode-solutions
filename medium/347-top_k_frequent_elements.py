class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initial Solution Idea
        # Get the frequency of each number in a hashmap
        # Key can be the integer and the values can be the frequency 
        # Sort all of these in a bucket with bucket[i] being the numbers that had that freq
        # Scan from end of bucket to start

        freq = {}
        bucket_arr = [None] * (len(nums) + 1)
        j = k
        output = []

        for num in nums:
            if freq.get(num) is not None:
                freq[num] += 1
            else:
                freq[num] = 1

        for key, value in freq.items():
            if bucket_arr[value] is not None:
                bucket_arr[value].append(key)
            else:
                bucket_arr[value] = [ key ]

        for bucket in bucket_arr[::-1]:
            if bucket is not None:
                if len(bucket) > 1:
                    for num in bucket[::-1]:
                        if k > 0:
                            k -= 1
                            output.append(num)
                else:
                    if k > 0:
                        output.append(bucket[0])
                        k -= 1

        return output
                

