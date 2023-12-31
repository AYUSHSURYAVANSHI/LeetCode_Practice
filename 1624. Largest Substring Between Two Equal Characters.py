class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        return (lambda d:max(i-d[c]-1 if c in d else d.update({c:i}) or -1 for i,c in enumerate(s)))({})