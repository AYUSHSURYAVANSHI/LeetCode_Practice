class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        g = cache(lambda prev:(gg:=lambda i,cur:i==m and [cur] or sum((gg(i+1,cur+cand) 
            for cand in 'rgb' if prev[i]!=cand and (i==0 or cur[-1]!=cand)),[]))(0,''))

        return (f:=cache(lambda j,prev:j==n or sum(f(j+1,cur) for cur in g(prev))%(10**9+7)))(0,'_'*m)