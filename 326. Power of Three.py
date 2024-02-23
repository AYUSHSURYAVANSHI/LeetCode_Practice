class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(-31,32):
            if n==(3**i):
                return True 
