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
        return int(ans, 2)