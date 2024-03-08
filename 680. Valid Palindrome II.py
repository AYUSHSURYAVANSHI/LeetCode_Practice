<<<<<<< HEAD
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                return s[:i]+s[i+1:] == (s[:i]+s[i+1:])[::-1] or s[:j]+s[j+1:] == (s[:j]+s[j+1:])[::-1]
            i+=1
            j-=1
=======
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                return s[:i]+s[i+1:] == (s[:i]+s[i+1:])[::-1] or s[:j]+s[j+1:] == (s[:j]+s[j+1:])[::-1]
            i+=1
            j-=1
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return True