class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars={}
        for char in s:
            if char in chars:
                chars[char]+=1
            else:
                chars[char]=1
        for char in t:
            if char not in chars:
                return False
            if char in chars:
                chars[char]-=1
                if chars[char]==0:
                    del chars[char]
        if chars:
            return False
        return True