from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        if len(intervals) == 1:
            return ans
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                ans += 1
                if intervals[i][1] > intervals[i - 1][1]:
                    intervals[i][1] = intervals[i - 1][1]
        return ans
