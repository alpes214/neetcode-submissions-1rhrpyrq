class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c for c in s.lower() if c.isalnum()]
        l = list(reversed(cleaned))
        if list(cleaned) == l:
            return True
        return False
