class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_map = {}
        max_length = 0

        l = 0
        for r in range(len(s)):
            character_map[s[r]] = 1 + character_map.get(s[r], 0)
        
            while (r - l + 1) - max(character_map.values()) > k:
                character_map[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)
            
        return max_length
