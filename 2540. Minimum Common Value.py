class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = set(nums1)
        m = set(nums2)
        try :
            return min(n.intersection(m))
        except ValueError:
            return -1