class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        for i in range(len(s)):
            curr = dict[s[i]]
            sum += curr

            if i>0 and curr > dict[s[i-1]]:
                sum -= (2*dict[s[i-1]])
        return sum 