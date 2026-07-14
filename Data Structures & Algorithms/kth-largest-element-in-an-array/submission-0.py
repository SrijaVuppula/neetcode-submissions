class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return nums[-1]
        if len(nums) >= 2:
            nums.sort()
            A = nums[-k]
            return A