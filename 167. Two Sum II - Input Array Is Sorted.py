<<<<<<< HEAD
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n, m  = 0,len(numbers) - 1
        while n < m:
            if numbers[n] + numbers[m] == target:
               return [n +1,m +1]
            if numbers[n] + numbers[m] < target:
                n += 1
            else :
=======
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n, m  = 0,len(numbers) - 1
        while n < m:
            if numbers[n] + numbers[m] == target:
               return [n +1,m +1]
            if numbers[n] + numbers[m] < target:
                n += 1
            else :
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
                m -= 1 