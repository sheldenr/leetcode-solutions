class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        i, j = 0, 0

        substring_set = set(s[0])
        longest_substring_size = 1

        for _ in range(len(s) * 2):
            if (j + 1) < len(s) and s[j + 1] in substring_set:
                substring_set.remove(s[i])
                i += 1
            elif (j + 1) < len(s):
                substring_set.add(s[j+1])
                j += 1

            longest_substring_size = max(longest_substring_size, len(substring_set))

        return longest_substring_size
