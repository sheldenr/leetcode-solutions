class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        freq_map = [0] * 26

        populate freq_map from magazine for char in ord(char) index

        look through ransomNote and decrement values in magazine at proper index

        return sum of freq_map == 0
        """

        freq_map = [0] * 26

        for letter in magazine:
            freq_map[ord(letter.lower()) - ord("a")] += 1

        for letter in ransomNote:
            freq_map[ord(letter.lower()) - ord("a")] -= 1

        for bucket in freq_map:
            if bucket < 0:
                return False
        
        return True
