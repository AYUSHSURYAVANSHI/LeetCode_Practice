class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        v1 = sum(val in nums2 for val in nums1)
        v2 = sum(val in nums1 for val in nums2)
      
        return [v1,v2]