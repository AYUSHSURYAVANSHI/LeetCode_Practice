<<<<<<< HEAD
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f1 = Counter(word1)
        f2 = Counter(word2)
        if f1.keys() != f2.keys():
            
            return False
=======
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f1 = Counter(word1)
        f2 = Counter(word2)
        if f1.keys() != f2.keys():
            
            return False
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return sorted(list(f1.values())) == sorted(list(f2.values()))