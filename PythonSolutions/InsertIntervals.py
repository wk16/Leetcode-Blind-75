from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x: x[0])
        ans = [intervals[0]]
        for interval in intervals:
            if interval[0]>ans[-1][1]:
                ans.append(interval)
            elif interval[1]>ans[-1][1]:
                ans[-1][1]=interval[1]
        return ans