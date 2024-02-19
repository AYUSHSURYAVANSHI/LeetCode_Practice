class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(-31,32):
            if n==(4**i):
                return True 
