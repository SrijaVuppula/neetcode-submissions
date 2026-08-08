class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) -1
        A = list()

        while(i < j):
            B = min(heights[i],heights[j]) * (j - i)
            A.append(B)
            if heights[i] < heights[j]:
                i = i + 1
            else:
                j = j - 1
        return max(A)