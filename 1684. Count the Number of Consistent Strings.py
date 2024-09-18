<<<<<<< HEAD
class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        arr = [0] * 26
        for c in allowed:
            arr[ord(c) - ord('a')] = 1
        
        count = 0
        for word in words:
            flag = 1
            for char in word:
                if arr[ord(char) - ord('a')] == 0:
                    flag = 0
                    break
            count += flag
=======
class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        arr = [0] * 26
        for c in allowed:
            arr[ord(c) - ord('a')] = 1
        
        count = 0
        for word in words:
            flag = 1
            for char in word:
                if arr[ord(char) - ord('a')] == 0:
                    flag = 0
                    break
            count += flag
>>>>>>> 53cbd46aa08ed51a116a277d334efcc0225e7e90
        return count