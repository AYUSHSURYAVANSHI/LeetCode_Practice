<<<<<<< HEAD
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k, i = k % sum(chalk), 0 # last iterative value of k before negative
        while k > 0:
            k -= chalk[i]
            if k < 0: return i  # return i here, since this is who needs to change the chalk
            i += 1
        return i # actually never reaches this step :-), just necessary for syntax

        #Technically 6 line solution haha
=======
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k, i = k % sum(chalk), 0 # last iterative value of k before negative
        while k > 0:
            k -= chalk[i]
            if k < 0: return i  # return i here, since this is who needs to change the chalk
            i += 1
        return i # actually never reaches this step :-), just necessary for syntax

        #Technically 6 line solution haha
>>>>>>> 53cbd46aa08ed51a116a277d334efcc0225e7e90
    