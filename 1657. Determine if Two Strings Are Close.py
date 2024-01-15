class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f1 = Counter(word1)
        f2 = Counter(word2)
        if f1.keys() != f2.keys():
            
            return False
        return sorted(list(f1.values())) == sorted(list(f2.values()))