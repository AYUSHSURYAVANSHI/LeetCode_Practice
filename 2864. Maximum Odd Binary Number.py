class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        length = len(s)
        count = s.count('1')

        res = []

        if count >= 1:
            count -= 1
            for i in range(length - 1):
                if i < count:
                    res.append('1')
                else:
                    res.append('0')
            res.append('1')


        return ''.join(res)