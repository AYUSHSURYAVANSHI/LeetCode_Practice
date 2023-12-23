<<<<<<< HEAD
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        num = high - low + 1
        
        if num & 1 == 1:
            if low & 1 == 1:
                return (num + 1 ) //  2
        return num // 2 
=======
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        num = high - low + 1
        
        if num & 1 == 1:
            if low & 1 == 1:
                return (num + 1 ) //  2
        return num // 2 
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        