class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = set()
        for n in nums:
            diff.add(target - n)

        for i in range(len(nums)):
            if target - nums[i] in diff:
                for j in range(len(nums)):
                    if nums[i] + nums[j] == target and i != j:
                        return [i, j]
