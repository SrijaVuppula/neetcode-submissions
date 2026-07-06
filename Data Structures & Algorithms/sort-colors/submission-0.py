class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        A = list()
        B = list()
        C = list()
        D = list()

        for i in range(len(nums)):
            if nums[i] == 0:
                A.append(nums[i])
            if nums[i] == 1:
                B.append(nums[i])
            if nums[i] == 2:
                C.append(nums[i]) 

        D = A + B + C 
        nums[:] = D
        return D