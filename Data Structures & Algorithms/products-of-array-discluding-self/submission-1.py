class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))
        prefix, suffix = 1, 1

        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]
            output[len(nums) - 1 - i] *= suffix
            suffix *= nums[len(nums) - 1 - i]

        return output
