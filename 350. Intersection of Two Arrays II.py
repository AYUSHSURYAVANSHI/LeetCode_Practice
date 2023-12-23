<<<<<<< HEAD
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list((set(nums1) & set(nums2)))  
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
=======
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list((set(nums1) & set(nums2)))  
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        return res