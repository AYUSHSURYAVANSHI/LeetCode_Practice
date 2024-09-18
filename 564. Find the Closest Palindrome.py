<<<<<<< HEAD
class Solution:
    def nearestPalindromic(self, n: str) -> str:
=======
class Solution:
    def nearestPalindromic(self, n: str) -> str:
>>>>>>> 53cbd46aa08ed51a116a277d334efcc0225e7e90
        return (l:=len(n),p:=int(n[:(l+1)//2])) and str(min({10**(l-1)-1,10**l+1,*(int((t:=str(p+q))+t[-1-l%2::-1]) for q in (-1,0,1))}-{n:=int(n)},key=lambda v:(abs(v-n),v)))