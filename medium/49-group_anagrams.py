class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Naive solution would be sorting each string and then comparing and grouping those
        # Not coding this atm

        # Optimal solution, freq array
        # This solution is taken from netecode, relearn this 
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(string)

        return list(res.values())
