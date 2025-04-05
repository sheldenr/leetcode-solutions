class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Certainly a really poor solution, im going to need to go through these one more time
        char_arr = []

        for char in s:
            if char.isalnum():
                char_arr.append(char.lower())


        return char_arr == char_arr[::-1]
