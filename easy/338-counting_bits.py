class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(n + 1):
            val = i
            weight = 0

            while val:
                val &= val - 1
                weight += 1

            ans[i] = weight
        
        return ans
