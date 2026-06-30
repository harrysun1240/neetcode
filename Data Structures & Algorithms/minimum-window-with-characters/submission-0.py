class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count_s = defaultdict(int)
        count_t = defaultdict(int)
        res = ""

        for c in t:
            count_t[c] += 1

        matches = 0
        l = 0
        for r in range(len(s)):
            index = s[r]
            count_s[index] += 1
            if index in count_t and count_s[index] == count_t[index]:
                matches += 1

            while matches == len(count_t):
                if r - l + 1 < len(res) or res == "":
                    res = s[l:r + 1]
                index = s[l]
                count_s[index] -= 1
                if index in count_t and count_s[index] < count_t[index]:
                    matches -= 1
                l += 1

        return res
