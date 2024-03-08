<<<<<<< HEAD
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        l=[set()]
        for i in arr:
            if len(set(i)) < len(i):
                continue
            i = set(i)
            for j in l:
                if i & j:
                    continue
                l.append(i | j)
        m = 0
        for i in l:
            if m < len(i):
                m = len(i)
=======
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        l=[set()]
        for i in arr:
            if len(set(i)) < len(i):
                continue
            i = set(i)
            for j in l:
                if i & j:
                    continue
                l.append(i | j)
        m = 0
        for i in l:
            if m < len(i):
                m = len(i)
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return m