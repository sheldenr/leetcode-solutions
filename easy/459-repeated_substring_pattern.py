class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:    
        test_string = s + s
        test_string = test_string[1:-1]

        return s in test_string
