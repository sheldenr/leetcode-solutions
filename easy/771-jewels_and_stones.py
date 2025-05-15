class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(list(jewels))
        res = 0

        for character in stones:
            if character in jewel_set:
                res += 1
        
        return res
