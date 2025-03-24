class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # # First sliding window problem (time limit exceeded, O(n*k))

        # max_avg = float('-inf')

        # for window_start in range(len(nums) - k + 1):
        #     if sum(nums[window_start:window_start + k]) / k > max_avg:
        #         max_avg = sum(nums[window_start:window_start + k]) / k
        
        # return max_avg

        # Second planned solution (idk i give up, lookup solution)
        # I know that the idea is calculate the first window (0 thru k) and then add on the k + 1 element and subtract the element before the window
        # do this and find the sum for each time so that it is a one pass and then return the greatest sum found
        max_sum = sum(nums[0:k])
        current_sum = max_sum

        for i in range(1, ):
            if max_sum + nums[k + i] - nums[i] > max_sum:
                max_sum = max_sum + nums[k + i] - nums[i]

        return max_sum / k
