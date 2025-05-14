class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        seen_sequences = set()
        duplicates = set()

        l = 0

        for r in range(9, len(s)):
            sequence = s[l : r + 1]
            if sequence in seen_sequences:
                duplicates.add(sequence)

            seen_sequences.add(sequence)
            
            l += 1

        return list(duplicates)
