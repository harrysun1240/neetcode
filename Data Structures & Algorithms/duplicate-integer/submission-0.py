import heapq

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        heapq.heapify(nums)
        if nums == []: return False
        a = heapq.heappop(nums)
        while nums:
            b = heapq.heappop(nums)
            if a == b: return True
            a = b
        return False
