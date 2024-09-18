<<<<<<< HEAD
class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()
        
        mask = (1 << bit_length) - 1
        
=======
class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()
        
        mask = (1 << bit_length) - 1
        
>>>>>>> 53cbd46aa08ed51a116a277d334efcc0225e7e90
        return num ^ mask