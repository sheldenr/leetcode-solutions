class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        output = -1

        for index, word in enumerate(words):
            if len(word) >= len(searchWord):
                if word[0:len(searchWord)] == searchWord:
                    output = (index + 1)
                    break

        return output
