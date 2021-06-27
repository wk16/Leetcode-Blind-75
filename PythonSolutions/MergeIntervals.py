from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0]>res[-1][1]:
                res.append(interval)
            if interval[1]>res[-1][1]:
                res[-1][1]= interval[1]
        return res