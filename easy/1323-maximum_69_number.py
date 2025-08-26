class Solution:
    def maximum69Number (self, num: int) -> int:
        # Find the leftmost integer than is a six and swap
        indexToSwap = -1
        numString = list(str(num))
        
        for index in range(len(numString)):
            if numString[index] == "6":
                indexToSwap = index
                break

        if indexToSwap == -1:
            return num
        else:
            numString[indexToSwap] = "9"
            return int(''.join(numString))
