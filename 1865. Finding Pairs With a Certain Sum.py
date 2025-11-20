class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.num1 = nums1
        self.num2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.freq[self.num2[index]] -= 1
        self.num2[index] += val
        self.freq[self.num2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.freq[tot - n] for n in self.num1)