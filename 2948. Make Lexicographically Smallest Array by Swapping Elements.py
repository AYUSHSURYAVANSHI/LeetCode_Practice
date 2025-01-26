class Solution:
    def lexicographicallySmallestArray(self, a: List[int], l: int) -> List[int]:
        vv,ii = zip(*sorted(zip(a+[inf], count())))
        for i,j in pairwise([0]+[i for i in range(1,len(vv)) if vv[i]-vv[i-1]>l]):
            for k,v in zip(sorted(ii[i:j]), vv[i:j]):
                a[k] = v
        
        return a