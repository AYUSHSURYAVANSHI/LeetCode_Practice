class Solution:
    def isPalindrome(self, x: int) -> bool:
       rev = str(x)
       if rev == rev[::-1]:
          return True 
       else:
           return False
