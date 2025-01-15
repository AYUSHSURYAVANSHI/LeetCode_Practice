class Solution:
    def countGoodStrings(self, l: int, h: int, z: int, o: int) -> int:
        return (f:=cache(lambda i:i<=h and ((i>=l)+f(i+z)+f(i+o))%(10**9+7)))(0)