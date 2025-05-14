class Solution:
    def characterReplacement(self, s: str, k: int) -> int:  
        character_map = { s[0] : 1 }
        max_size = 1
        l = 0

        for r in range(1, len(s)):
            # r always increases, if window size (r-l) - most_freq_char < k, keep l same, else increase l
            if character_map.get(s[r]) == None:
                character_map[s[r]] = 1
            else:
                character_map[s[r]] += 1
            
            largest_occurence = max(character_map.values())
            

            if (r - l) - largest_occurence >= k:
                character_map[s[l]] -= 1
                l += 1

            max_size = max(max_size, (r - l + 1))

        return max_size
            
