class Solution:
    def firstUniqChar(self, s: str) -> int:
        character_map = DefaultDict(int)

        for char in s:
            character_map[char] += 1

        for index, char in enumerate(s):
            if character_map[char] == 1:
                return index

        return -1
