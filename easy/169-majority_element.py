class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = defaultdict(int)

        for num in nums:
            count_map[num] += 1

        return max(count_map, key=count_map.get)
