class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = 0

        # Find the largest power that is smaller or equal to n
        while 3**power <= n:
            power += 1

        while n > 0:
            # Subtract current power from n
            if n >= 3**power:
                n -= 3**power
            # We cannot use the same power twice
            if n >= 3**power:
                return False
            # Move to the next lower power
            power -= 1

        # n has reached 0
        return True