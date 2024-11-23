<<<<<<< HEAD
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
=======
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
>>>>>>> d6f8e7f5bf95ec30dd893de1512f2b076cbb6786
        return goal in s + s