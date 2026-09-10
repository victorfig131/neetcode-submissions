class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = len(nums) * [1]
        suffix = len(nums) * [1]
        output = len(nums) * [1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]

        return output