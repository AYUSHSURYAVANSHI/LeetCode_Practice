<<<<<<< HEAD
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


=======
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


>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return ''.join(res)