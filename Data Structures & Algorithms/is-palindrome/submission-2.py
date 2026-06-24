class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        l = 0

        s = s.lower()

        while l < r: 
            while s[r].isalnum() != True and l < r:
                r -= 1
            while s[l].isalnum() != True and l < r:
                l += 1
            if s[r] != s[l]:
                return False

            r -= 1
            l += 1
        return True