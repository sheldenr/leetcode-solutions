class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consec = 0
        
        for num in arr:
            if num % 2 != 0: # Odd
                consec += 1
            else:
                consec = 0

            if consec == 3:
                return True

        return False
