class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list((set(nums1) & set(nums2)))  
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
        return res