class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2) - len(s1) + 1):
            j = 0
            temp = s1
            while s2[i + j] in temp:
                temp = temp.replace(s2[i + j], "", 1)
                if temp == "":
                    return True
                j += 1
        return False
