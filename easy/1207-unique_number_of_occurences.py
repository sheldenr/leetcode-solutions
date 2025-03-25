class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        counts, counts_without_dup = [], []
        
        for val in arr:
            if occurences.get(val) == None:
                occurences[val] = 1
            else:
                occurences[val] += 1
        
        for key in occurences:
            counts.append(occurences[key])

        return len(counts) == len(set(counts))
