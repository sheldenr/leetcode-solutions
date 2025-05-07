class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # Determine sorted portion
            if nums[l] <= nums[mid]: #Left is sorted
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
