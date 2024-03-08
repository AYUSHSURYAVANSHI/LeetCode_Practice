<<<<<<< HEAD
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if len(bin(left)) != len(bin(right)):
            return 0

        l = bin(left)
        r = bin(right)

        ans = ''
        for i in range(len(r)):
            if l[i] == r[i]:
                ans += l[i]
            else:
                ans += '0'*(len(r)-i)
                return int(ans, 2)
=======
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if len(bin(left)) != len(bin(right)):
            return 0

        l = bin(left)
        r = bin(right)

        ans = ''
        for i in range(len(r)):
            if l[i] == r[i]:
                ans += l[i]
            else:
                ans += '0'*(len(r)-i)
                return int(ans, 2)
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return int(ans, 2)