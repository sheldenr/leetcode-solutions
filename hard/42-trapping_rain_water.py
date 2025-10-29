class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max_arr = [0] * n
        right_max_arr = [0] * n
        res = 0

        max_val = 0
        for i in range(len(height)):
            max_val = max(height[i], max_val)
            left_max_arr[i] = max_val
 
        max_val = 0
        for i in range(len(height) -1, -1, -1):
            max_val = max(height[i], max_val)
            right_max_arr[i] = max_val

        for i in range(len(height)):
            if (i != 0) or( i != (n-1)):
                min_point = min(right_max_arr[i], left_max_arr[i])
                res += max(min_point - height[i], 0)
        
        return res
