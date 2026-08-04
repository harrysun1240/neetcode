class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            res = self.canFinish(piles, h, mid)
            if res:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def canFinish(self, piles: List[int], h: int, k: int) -> bool:
        count = 0
        for num in piles:
            count += math.ceil(num / k)
        return count <= h
