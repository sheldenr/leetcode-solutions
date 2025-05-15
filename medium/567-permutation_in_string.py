class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window of length len(s1) through s2
        # Use set of characters to determine if permutation

        if len(s1) > len(s2):
            return False

        s1_map = {}
        s2_map = {}

        for char in s1:
            if s1_map.get(char) == None:
                s1_map[char] = 1
            else:
                s1_map[char] += 1

        for i in range(len(s1)):
            if s2_map.get(s2[i]) == None:
                s2_map[s2[i]] = 1
            else:
                s2_map[s2[i]] += 1
        
        if s1_map == s2_map:
            return True

        for i in range(len(s1), len(s2)):
            if s2_map.get(s2[i]) == None:
                s2_map[s2[i]] = 1
            else:
                s2_map[s2[i]] += 1

            s2_map[s2[i - len(s1)]] -= 1

            if s2_map[s2[i - len(s1)]] == 0:
                del s2_map[s2[i - len(s1)]]

            if s1_map == s2_map:
                return True

        return False
