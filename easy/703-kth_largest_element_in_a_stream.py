import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initialize heap
        self.heap = list(nums)
        self.k = k
        heapq.heapify(self.heap)

        # Remove elemenets until heap is at most size k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Add element
        heapq.heappush(self.heap, val)
        
        # Remove elements if heap is greater than size k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Return min from minheap
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
