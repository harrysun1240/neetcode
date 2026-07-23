class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            pairs.append((position[i], speed[i], time))
        pairs.sort()

        curr_max = 0
        res = 0
        for i in range(len(pairs) - 1, -1, -1):
            if pairs[i][2] > curr_max:
                curr_max = pairs[i][2]
                res += 1

        return res
