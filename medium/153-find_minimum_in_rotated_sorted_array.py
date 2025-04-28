class Solution:
    def findMin(self, nums: List[int]) -> int:
        heap = nums
        heapify(heap)
        return heappop(heap)
