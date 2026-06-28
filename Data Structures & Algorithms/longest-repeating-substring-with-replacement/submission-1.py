class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            c, j, l = 1, i + 1, k
            while j < len(s):
                if s[j] != s[i]:
                    if l == 0:
                        break
                    l -= 1
                j += 1
                c += 1
            res = max(res, min(c + l, len(s)))
        return res
