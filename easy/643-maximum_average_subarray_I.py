class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # # First sliding window problem (time limit exceeded, O(n*k))

        # max_avg = float('-inf')

        # for window_start in range(len(nums) - k + 1):
        #     if sum(nums[window_start:window_start + k]) / k > max_avg:
        #         max_avg = sum(nums[window_start:window_start + k]) / k
        
        # return max_avg

        # Second planned solution (idk i give up, lookup solution)
        max_sum = sum(nums[0:k])

        for i in range(len(nums) - k):
            if max_sum + nums[k + i] - nums[i] > max_sum:
                max_sum = max_sum + nums[k + i] - nums[i]

        return max_sum / k
