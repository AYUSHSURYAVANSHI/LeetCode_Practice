<<<<<<< HEAD
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        S = sorted(arr,key = lambda x:(c[x],x))
=======
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        S = sorted(arr,key = lambda x:(c[x],x))
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return len(set(S[k:]))