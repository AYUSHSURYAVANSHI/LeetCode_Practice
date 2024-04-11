class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r = 0
        for c in s:
            r ^= ord(c)
        for c in t:
            r ^= ord(c)
        return chr(r)