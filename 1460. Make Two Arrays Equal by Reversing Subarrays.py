<<<<<<< HEAD
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
=======
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
>>>>>>> 45936108b93e7559b13be06f63781db262708cea
        return Counter(target) == Counter(arr)