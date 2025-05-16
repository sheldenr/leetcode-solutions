class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        shortest_len = float("inf")

        for s in strs:
            if len(s) < shortest_len:
                shortest_len = len(s)

        for i in range(shortest_len):
            prefixes = set()

            for s in strs:    
                prefixes.add(s[i])
            
            if len(prefixes) > 1:
                break
            else:
                prefix += prefixes.pop()

        return prefix
                
