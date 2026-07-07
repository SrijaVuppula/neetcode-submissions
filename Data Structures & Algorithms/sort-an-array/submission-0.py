class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        A = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A.append(left[i])
                i = i + 1
            else:
                A.append(right[j])
                j = j + 1
        A = A + left[i:]
        A = A + right[j:]
        return A