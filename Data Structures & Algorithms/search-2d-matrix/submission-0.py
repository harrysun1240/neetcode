import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = [num for row in matrix for num in row]
        index = bisect.bisect_left(flattened, target)
        return True if index < len(flattened) and flattened[index] == target else False
