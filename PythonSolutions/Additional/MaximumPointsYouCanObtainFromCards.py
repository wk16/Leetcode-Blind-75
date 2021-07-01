from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l,r=0,len(cardPoints)-k
        res=sum(cardPoints[r:])
        temp = res
        while r<len(cardPoints):
            temp += cardPoints[l]-cardPoints[r]
            res=max(res,temp)
            l+=1
            r+=1
        return res