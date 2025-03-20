class Solution:
    def reverseWords(self, s: str) -> str:
        # # Initial solution
        # word_arr = s.lstrip().rstrip().split(" ")
        # output_string = ""

        # for word_index in range(len(word_arr) - 1, -1, -1):
        #     if word_arr[word_index].isalnum():
        #         output_string += word_arr[word_index] + " "

        # output_string = output_string.rstrip()

        # return output_string

        # Better solution post-research
        s = s.strip()
        words = s.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

        # Learnings ------------
        # s.strip() works, no need for s.lstrip() and s.rstrip()
        # s.split() works even for multiple whitespaces in a row, no need to check if alnum
        # join() syntax kind of unintuitive in my opinion
            # nvm i take it back
