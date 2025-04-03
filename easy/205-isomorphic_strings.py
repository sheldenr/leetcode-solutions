class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st_map, ts_map = {}, {}
        n = len(s)
        
        for i in range(n):
            char1, char2 = s[i], t[i]

            if (char1 in st_map and st_map[char1] != char2) or (char2 in ts_map and ts_map[char2] != char1):
                return False

            st_map[char1] = char2
            ts_map[char2] = char1

        return True
