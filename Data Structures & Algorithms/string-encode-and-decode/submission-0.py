class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for i in range(len(strs)):
            enc += str(len(strs[i])) + "#" + strs[i] + " "
        return enc

    def decode(self, s: str) -> List[str]:
        length_str = ""
        word = ""
        rec = False
        res = []
        for i in range(len(s)):
            if rec == False:
                if s[i] == "#":
                    length = int(length_str)
                    length_str = ""
                    rec = True
                else:
                    length_str += s[i]
            else:
                if len(word) == length:
                    res.append(word)
                    word = ""
                    rec = False
                else:
                    word += s[i]
        return res
