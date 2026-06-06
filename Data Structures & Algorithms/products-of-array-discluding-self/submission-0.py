class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = math.prod([nums[n] for n in range(len(nums)) if n != i])
        return output