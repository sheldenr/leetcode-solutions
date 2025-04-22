class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_len = float('inf')
        num_of_strings = len(strs)
        output = ""

        for string in strs:
            if len(string) <= smallest_len:
                smallest_len = len(string)
            
        # for i in range(num_of_strings):
        #     for j in range(int(smallest_len)):

