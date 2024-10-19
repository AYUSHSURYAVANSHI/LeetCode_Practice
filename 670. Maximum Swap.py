class Solution:
    def maximumSwap(self, v: int) -> int:
        res = s = str(v)
        for i,c in enumerate(s):
            for j in range(i+1,len(s)):
                res = max(res, s[:i]+s[j]+s[i+1:j]+c+s[j+1:])
        
        return int(res)
    