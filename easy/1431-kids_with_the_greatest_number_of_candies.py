class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        res = [False] * len(candies)

        print(res)

        for index, val in enumerate(candies):
            if val + extraCandies >= max_num:
                res[index] = True

        return res
