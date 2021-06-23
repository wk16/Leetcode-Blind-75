class Solution:
    def helper(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j - i - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            temp = max(self.helper(s, i, i), self.helper(s, i, i + 1))
            if temp > end - start:
                start = i - (temp - 1) // 2
                end = i + temp // 2
        return s[start:end + 1]