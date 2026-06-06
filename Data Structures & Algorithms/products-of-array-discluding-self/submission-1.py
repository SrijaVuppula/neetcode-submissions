class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        A = 1
        B = 1
        for i in range(len(nums)):
            output[i] = A
            A *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= B
            B *= nums[i]
        return output