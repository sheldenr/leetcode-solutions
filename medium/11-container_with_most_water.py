class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i, j = 0, len(height) - 1
        
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_area = max(area, max_area)

            # Move the pointer that has the smaller height
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
        return max_area

