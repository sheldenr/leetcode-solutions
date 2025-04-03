class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list, output = [], list(s)
        vowels = set(["a", "e", "i", "o", "u"])

        for char in s:
            if char.lower() in vowels:
                vowel_list.append(char)

        for index, char in enumerate(s):
            if char.lower() in vowels:
                output[index] = vowel_list.pop()

        return "".join(output)
