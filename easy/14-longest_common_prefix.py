class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        string -> string
        """

        res = []
        min_length = len(strs[0])

        for s in strs:
            min_length = min(len(s), min_length)

        for i in range(min_length):
            for s in strs:
                curr = strs[0][i]

                if s[i] != curr:
                    return "".join(res)
                
            res.append(curr)

        return "".join(res)
