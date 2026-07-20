class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        A = {} 
        for i, x in enumerate(numbers, start = 1):  
            B = target - x
            if B in A: 
                return [A[B], i]
            else:
                A[x] = i