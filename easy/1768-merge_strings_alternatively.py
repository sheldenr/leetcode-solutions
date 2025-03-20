class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # # Initial solution that initially checks length and uses for loop and appends rest
        # merged = ""
        # merged_str_len = len(word1) + len(word2)

        # if len(word1) == len(word2):
        #     for i in range(len(word1)):
        #         merged += word1[i]
        #         merged += word2[i]

        # if len(word1) > len(word2):
        #     for i in range(len(word2)):
        #         merged += word1[i]
        #         merged += word2[i]
        #     merged += word1[len(word2):]

        # if len(word1) < len(word2):
        #     for i in range(len(word1)):
        #         merged += word1[i]
        #         merged += word2[i]
        #     merged += word2[len(word1):]

        # return merged



        # Solution after learning of two pointer approach
	# O(m+n) time and space complexity
        merged = ""
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            merged += word1[i]
            merged += word2[j]
            i += 1
            j += 1

        if i < len(word1):
            merged += word1[len(word2):]
        else: 
            merged += word2[len(word1):]

        return merged
