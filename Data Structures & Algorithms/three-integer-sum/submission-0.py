class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        A = sorted(nums)
        B = list()

        for i in range(len(A)):
            if i > 0 and A[i] == A[i-1]:
                continue
            j = i + 1
            k = len(A) - 1
            while (j < k):
                C = A[i] + A[j] + A[k]
                if C == 0:
                    B.append([A[i], A[j], A[k]])
                    j = j + 1
                    k = k - 1
                    while j < k and A[j] == A[j-1]:
                        j = j + 1  
                    while j < k and A[k] == A[k+1]:
                        k = k - 1  
                elif C > 0:
                    k = k -1
                else:
                    j = j + 1
        return B