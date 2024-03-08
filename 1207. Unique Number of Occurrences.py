<<<<<<< HEAD
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        memo = []
        for i in Counter(arr).values():
            if i in memo:
                return False
            else:
                memo.append(i)
=======
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        memo = []
        for i in Counter(arr).values():
            if i in memo:
                return False
            else:
                memo.append(i)
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return True