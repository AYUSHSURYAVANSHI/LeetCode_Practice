class Solution:
    def minOperations(self, s: str) -> int:
        return min((n := sum(i % 2 == int(c) for i , c in enumerate(s))), len(s)-n)