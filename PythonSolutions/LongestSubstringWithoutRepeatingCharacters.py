class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, start = 0, 0
        used = {}
        for i, char in enumerate(s):
            if char in used and used[char]>=start:
                start = used[char] + 1
                used[char]=i
            else:
                used[char]=i
                if longest<i-start + 1:
                    longest = i-start + 1
        return longest