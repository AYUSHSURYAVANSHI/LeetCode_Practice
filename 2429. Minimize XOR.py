<<<<<<< HEAD
class Solution(object):
    def minimizeXor(self, num1, num2):
        a, b = bin(num1).count('1'), bin(num2).count('1')
        res = num1
        for i in range(32):
            if a > b and (1 << i) & num1 > 0:
                res ^= 1 << i
                a -= 1
            if a < b and (1 << i) & num1 == 0:
                res ^= 1 << i
                a += 1
=======
class Solution(object):
    def minimizeXor(self, num1, num2):
        a, b = bin(num1).count('1'), bin(num2).count('1')
        res = num1
        for i in range(32):
            if a > b and (1 << i) & num1 > 0:
                res ^= 1 << i
                a -= 1
            if a < b and (1 << i) & num1 == 0:
                res ^= 1 << i
                a += 1
>>>>>>> e8d3d9d9eca520160d3d8dacfb895cc1c9483c33
        return res