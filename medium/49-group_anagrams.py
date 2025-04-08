class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Unoptimal solution
        # Sort each string and store as keys in a hashmap
        # Store the values of the strings in appropriate key
        # Return list of values

        # counter = {}

        # for s in strs:
        #     sorted_s = "".join(sorted(s))
        #     if counter.get(sorted_s) == None:
        #         counter[sorted_s] = [s]
        #     else:
        #         counter[sorted_s].append(s)

        # return list(counter.values())



        # Optimal Solution
        # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create a frequency list for each of the strings as the signature
        # Create a hashmap with the signature as the key and pair the strings to the

        anagram_groups = {}

        for s in strs:
            frequency_array = [0] * 26 # Stores count for char at proper index

            for char in s:
                frequency_array[ord(char) - ord("a")] += 1

            frequency_tuple = tuple(frequency_array)

            if anagram_groups.get(frequency_tuple) == None:
                anagram_groups[frequency_tuple] = [s]
            else:


