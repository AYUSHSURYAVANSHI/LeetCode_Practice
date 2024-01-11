class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        ls=[0,1]
        i=2
        while ls[i-1]<=k:
            ls.append(ls[i-1]+ls[i-2])
            i+=1
        i-=1
        result=0
        while k>0:
            if ls[i]<=k:
                k-=ls[i]
                result+=1
            else:
                i-=1
        return result