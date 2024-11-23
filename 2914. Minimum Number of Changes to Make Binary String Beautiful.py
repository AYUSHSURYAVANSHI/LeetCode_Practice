<<<<<<< HEAD
class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i]!=s[i+1] for i in range(0, len(s), 2))
=======
class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i]!=s[i+1] for i in range(0, len(s), 2))
>>>>>>> d6f8e7f5bf95ec30dd893de1512f2b076cbb6786
        