class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c for c in s.lower() if c.isalnum()]
        if cleaned == cleaned[::-1]:
            return True
        return False
