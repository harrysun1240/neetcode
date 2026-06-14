class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ascs = []
        for s in strs:
            asc = []
            for i in range(len(s)):
                asc.append(ord(s[i]))
            asc.sort()
            ascs.append(asc)

        anss = []
        strs_copy = strs[:]
        i = 0
        while i < len(ascs):
            curr = ascs[i]
            ans = []
            j = i
            while j < len(ascs):
                if ascs[j] == curr:
                    ans.append(strs_copy[j])
                    ascs.pop(j)
                    strs_copy.pop(j)
                else:
                    j += 1
            anss.append(ans)
        return anss
