class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        i = 0
        while height[i] == 0:
            i += 1
            if i == len(height):
                return 0

        j = i + 1
        temp = 0
        while j != len(height):
            if height[j] >= height[i]:
                res += temp
                i = j
                temp = 0
            else:
                temp += height[i] - height[j]
            j += 1

        l = len(height) - 1
        while height[l] == 0:
            l -= 1

        k = l - 1
        temp = 0
        while k != i - 1:
            if height[k] >= height[l]:
                res += temp
                l = k
                temp = 0
            else:
                temp += height[l] - height[k]
            k -= 1

        return res
