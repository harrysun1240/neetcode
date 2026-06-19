class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        max_streak = 0
        for num in unique:
            current_streak = 1
            if num - 1 not in unique:
                current_num = num
                while current_num + 1 in unique:
                    current_num += 1
                    current_streak += 1
            max_streak = max(max_streak, current_streak)
        return max_streak
