class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lower_s = s.lower()
        new_s = ''.join(c for c in lower_s if c.isalnum())

        return new_s == new_s[::-1]
