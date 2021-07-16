from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * len(s)
        for word in wordDict:
            if word == s[:len(word)]:
                dp[len(word) - 1] = 1
        for i in range(0, len(dp)):
            if dp[i] == 1:
                for word in wordDict:
                    if word == s[i + 1:i + len(word) + 1]:
                        dp[i + len(word)] = 1
        print(dp)
        if dp[-1] == 1:
            return True
        return False
