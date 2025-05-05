class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Gather flattened array
        flattened_list = []
        for row in matrix:
            for element in row:
                flattened_list.append(element)

        # Do a binary search of the array
        l, r = 0, len(flattened_list) - 1
        mid = (l + r) // 2

        while l <= r:
            mid = (l + r) // 2

            if flattened_list[mid] == target:
                return True

            elif flattened_list[mid] > target:
                r = mid - 1

            elif flattened_list[mid] < target:
                l = mid + 1

        return False
        
        
