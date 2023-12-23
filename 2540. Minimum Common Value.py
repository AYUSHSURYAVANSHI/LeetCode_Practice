<<<<<<< HEAD
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = set(nums1)
        m = set(nums2)
        try :
            return min(n.intersection(m))
        except ValueError:
=======
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = set(nums1)
        m = set(nums2)
        try :
            return min(n.intersection(m))
        except ValueError:
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
            return -1