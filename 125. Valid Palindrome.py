<<<<<<< HEAD
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for i in s:
            if False == i.isalnum():
                s = s.replace(i,"")
        if s == s[::-1]:
            return True
=======
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for i in s:
            if False == i.isalnum():
                s = s.replace(i,"")
        if s == s[::-1]:
            return True
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return False