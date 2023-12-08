class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n, m  = 0,len(numbers) - 1
        while n < m:
            if numbers[n] + numbers[m] == target:
               return [n +1,m +1]
            if numbers[n] + numbers[m] < target:
                n += 1
            else :
                m -= 1 