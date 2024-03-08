<<<<<<< HEAD
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = defaultdict(int)
        
        for m in matches:
            lost[m[0]] += 0
            lost[m[1]] += 1
        
        zero = sorted([k for k, l in lost.items() if l == 0])
        ones = sorted([k for k, l in lost.items() if l == 1])
        
=======
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = defaultdict(int)
        
        for m in matches:
            lost[m[0]] += 0
            lost[m[1]] += 1
        
        zero = sorted([k for k, l in lost.items() if l == 0])
        ones = sorted([k for k, l in lost.items() if l == 1])
        
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return [zero, ones]