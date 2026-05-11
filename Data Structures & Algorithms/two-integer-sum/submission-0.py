class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}

        for i,x in enumerate(nums):
            B = target -x
            if B in A:
                return [A[B],i]
            else:
                A[x] = i