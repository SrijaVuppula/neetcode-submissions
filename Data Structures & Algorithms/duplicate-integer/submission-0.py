class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        A = set()

        for i in nums:
            if i in A:
                return True
            else:
                A.add(i)
        return False 