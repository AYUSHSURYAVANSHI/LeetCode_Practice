<<<<<<< HEAD
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraywithMostkDistinct(nums,k)-self.subarraywithMostkDistinct(nums,k-1)
    def subarraywithMostkDistinct(self,nums,k):
        left=0
        res=0
        ht=defaultdict(int)
        for right, num in enumerate(nums):
            ht[num] += 1
            while len(ht) > k:
                ht[nums[left]] -= 1
                if not ht[nums[left]]:
                    del ht[nums[left]]
                left += 1
            res += right - left + 1
=======
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraywithMostkDistinct(nums,k)-self.subarraywithMostkDistinct(nums,k-1)
    def subarraywithMostkDistinct(self,nums,k):
        left=0
        res=0
        ht=defaultdict(int)
        for right, num in enumerate(nums):
            ht[num] += 1
            while len(ht) > k:
                ht[nums[left]] -= 1
                if not ht[nums[left]]:
                    del ht[nums[left]]
                left += 1
            res += right - left + 1
>>>>>>> 10b2a6e3a579911ea69ba00fe2504f56a3a8b313
        return res