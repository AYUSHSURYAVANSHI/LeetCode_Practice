class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        S = sorted(arr,key = lambda x:(c[x],x))
        return len(set(S[k:]))