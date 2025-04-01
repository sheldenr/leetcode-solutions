class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # # Initial plan, calc sum from left and right incrementally and return when equivalent. 
        
        # # Very unoptimal solution
        # left_sum, right_sum = 0, 0

        # for i in range(len(nums)):
        #     # Left sum
        #     left_sum = sum(nums[:i])

        #     # Right sum
        #     right_sum = sum(nums[i+1:])

        #     # Check if equivalent
        #     if left_sum == right_sum:
        #         return i

        # return -1

        # # Plan Two (Hopefully Optimal)
        # # Calculate the sum once, and then find left and right sum by incr. based on current index
        # # This solution is dogshit, please come back to this
        
        # left_sum, right_sum = 0, sum(nums) - nums[0]

        # for i in range(len(nums)):
        #     if left_sum == right_sum:
        #         return i

        #     left_sum += nums[i]
        #     try:
        #         right_sum -= nums[i+1]
        #     except:
        #         break
        #     print(left_sum, right_sum)
        
        # return -1

        # ok im coming back to it, what is this
        # i got it, took a long time, make sure to actually think through test cases first bc that was bad
        left_sum, right_sum = 0, sum(nums) - nums[0]

        if left_sum == right_sum:
            return 0
        
        for i in range(1, len(nums)):
            left_sum += nums[i - 1]
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i    
            
        return -1

                


