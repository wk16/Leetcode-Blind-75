import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        ans = heapq.nlargest(k, count.keys(), key=count.get)
        return ans