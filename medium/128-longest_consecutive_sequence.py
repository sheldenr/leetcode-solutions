class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueElements = set(nums)
        longestSequence = 1

        if len(nums) == 0:
            longestSequence = 0

        for num in uniqueElements:
            streak = 1

            if (num - 1) not in uniqueElements:
                nextNum = num + 1

                while nextNum in uniqueElements:
                    streak += 1
                    nextNum += 1
            
            if streak > longestSequence:
                longestSequence = streak

        return longestSequence
