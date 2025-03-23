class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Initial implementation plan
        # I know this is a prefix sum problem (idk what that means)
        # I can find the altitude values through in O(n) time and find the max value in that array 
        altitude_val, altitudes = 0, [0]

        for index, val in enumerate(gain):
            altitude_val += gain[index]
            altitudes.append(altitude_val)

        return max(altitudes)
