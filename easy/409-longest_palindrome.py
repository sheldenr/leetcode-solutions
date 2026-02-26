class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = {}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        length = 0
        has_odd = False
        
        for count in char_counts.values():
            if count % 2 == 0:
                length += count
            else:
                # Add the even part of the odd count (e.g., if count is 7, add 6)
                length += count - 1
                has_odd = True
        
        # If we found at least one odd count, we can put one char in the middle
        if has_odd:
            length += 1
            
        return length