class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, max_repeat = 0, 0
        freq = {}
        if len(s) <= k:
            return len(s)
        l = 0
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
            max_repeat = max(max_repeat, freq[s[r]])
            if r - l + 1 - max_repeat > k:
                freq[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)
        return ans
