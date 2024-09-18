<<<<<<< HEAD
class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """

        xor_result = start ^ goal
        count = 0
        
        while xor_result > 0:
            count += xor_result & 1  
            xor_result >>= 1     
        
=======
class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """

        xor_result = start ^ goal
        count = 0
        
        while xor_result > 0:
            count += xor_result & 1  
            xor_result >>= 1     
        
>>>>>>> 53cbd46aa08ed51a116a277d334efcc0225e7e90
        return count