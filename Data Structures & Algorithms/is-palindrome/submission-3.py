class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i <= j:
            if ord(s[i]) < 48 or (57 < ord(s[i]) and ord(s[i]) < 65) or (90 < ord(s[i]) and ord(s[i]) < 97) or ord(s[i]) > 122:
                i += 1
                continue
            if ord(s[j]) < 48 or (57 < ord(s[j]) and ord(s[j]) < 65) or (90 < ord(s[j]) and ord(s[j]) < 97) or ord(s[j]) > 122:
                j -= 1
                continue
            if s[i] == s[j] or (ord(s[i]) >= 65 and ord(s[j]) >= 65 and abs(ord(s[i]) - ord(s[j])) == 32):
                i += 1
                j -= 1
                continue
            return False
        return True
