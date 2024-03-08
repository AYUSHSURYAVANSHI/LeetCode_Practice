<<<<<<< HEAD
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n + 1)

        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1
        
        for i in range(1, n + 1):
            if trusted[i] == n - 1:
                return i
        
=======
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n + 1)

        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1
        
        for i in range(1, n + 1):
            if trusted[i] == n - 1:
                return i
        
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return -1