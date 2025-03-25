class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Vowel set for constant access time (may not be useful because of small list size)
        vowel_set = set(["a", "e", "i", "o", "u"])

        # Sliding window approach for substring
        vowels, max_vowel_count = 0, 0
        
        for char in s[0:k]:
            if char in vowel_set:
                vowels += 1

        max_vowel_count = vowels

        for i in range(k, len(s)): 
            if s[i] in vowel_set:
                vowels += 1
            
            if s[i - k] in vowel_set:
                vowels -= 1

            max_vowel_count = max(max_vowel_count, vowels)

        return max_vowel_count
