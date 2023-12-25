class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def solve(i):
            if i>len(s)-1 : return 1
            curr = 0
            for j in (1,2):
                if i+j <=len(s) and s[i]!='0' and 1<=int(s[i:i+j])<=26 :
                    curr += solve(i+j)
            return curr
        return solve(0)