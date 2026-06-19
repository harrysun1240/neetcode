class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = []
        suffix_sum = []
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            suffix *= nums[len(nums) - i - 1]
            prefix_sum.append(prefix)
            suffix_sum.append(suffix)

        output = [suffix_sum[len(nums) - 2]]
        for i in range(1, len(nums) - 1):
            output.append(prefix_sum[i - 1] * suffix_sum[len(nums) - i - 2])
        output.append(prefix_sum[len(nums) - 2])

        return output
