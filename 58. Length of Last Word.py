<<<<<<< HEAD
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        
        if not words:
            return 0
        
=======
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        
        if not words:
            return 0
        
>>>>>>> 10b2a6e3a579911ea69ba00fe2504f56a3a8b313
        return len(words[-1])