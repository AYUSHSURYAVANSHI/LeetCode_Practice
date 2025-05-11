class Solution:
    def threeConsecutiveOdds(self, a):
        c = 0
        for x in a:
            c = c + 1 if x % 2 else 0
            if c == 3:
                return True
        return False