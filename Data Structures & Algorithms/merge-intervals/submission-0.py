class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        if len(intervals) > 1:
            A = intervals.sort()
            i = 0
            B = []
            for intervals in intervals:
                if B and intervals[0] <= B[-1][1]:
                    B[-1][1] = max(B[-1][1], intervals[1])
                else:
                    B.append(intervals)
        return B