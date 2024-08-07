<<<<<<< HEAD
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        count: list[int] = [0 for _ in range(201)]
        for num in nums:
            count[num + 100] += 1
        nums.sort(key=lambda val: (count[val + 100], -val))
=======
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        count: list[int] = [0 for _ in range(201)]
        for num in nums:
            count[num + 100] += 1
        nums.sort(key=lambda val: (count[val + 100], -val))
>>>>>>> 45936108b93e7559b13be06f63781db262708cea
        return nums