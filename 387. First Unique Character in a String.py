<<<<<<< HEAD
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ump = {}
        
        # Count character frequencies
        for char in s:
            ump[char] = ump.get(char, 0) + 1
        
        # Find the first unique character
        for i, char in enumerate(s):
            if ump[char] == 1:
                return i
        
        # If no unique character is found
=======
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ump = {}
        
        # Count character frequencies
        for char in s:
            ump[char] = ump.get(char, 0) + 1
        
        # Find the first unique character
        for i, char in enumerate(s):
            if ump[char] == 1:
                return i
        
        # If no unique character is found
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return -1