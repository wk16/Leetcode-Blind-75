class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPal(i, j):
            count=0
            while i>=0 and j<len(s) and s[i]==s[j] :
                count+=1
                i-=1
                j+=1
            return count
        res = 1
        for i in range(1,len(s)):
            res+=isPal(i-1,i)
            res+=isPal(i,i)
        return res