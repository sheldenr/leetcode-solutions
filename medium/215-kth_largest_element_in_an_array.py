class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # This solution took me forever just because of the fact that I do not understand how to proeprly implement a maxheap using python's minheap heapq implementation.
        heap = []
        heapify(heap)

        for num in nums:
            heappush(heap, -1 * num)
        
        for i in range(k - 1):
            heappop(heap)
        
        return -1 * heappop(heap)
