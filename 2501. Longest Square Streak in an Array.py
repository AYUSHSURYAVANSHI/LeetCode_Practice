<<<<<<< HEAD
class Solution:
    def longestSquareStreak(self, nums):
        mp = {}
        nums.sort()
        res = -1

        for num in nums:
            sqrt = isqrt(num)

            if sqrt * sqrt == num and sqrt in mp:
                mp[num] = mp[sqrt] + 1
                res = max(res, mp[num])
            else:
                mp[num] = 1

=======
class Solution:
    def longestSquareStreak(self, nums):
        mp = {}
        nums.sort()
        res = -1

        for num in nums:
            sqrt = isqrt(num)

            if sqrt * sqrt == num and sqrt in mp:
                mp[num] = mp[sqrt] + 1
                res = max(res, mp[num])
            else:
                mp[num] = 1

>>>>>>> d6f8e7f5bf95ec30dd893de1512f2b076cbb6786
        return res