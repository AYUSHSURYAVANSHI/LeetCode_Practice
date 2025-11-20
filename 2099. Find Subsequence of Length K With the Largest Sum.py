class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Pair each value with its original index
        indexed = [(val, idx) for idx, val in enumerate(nums)]

        # Step 2: Sort by value descending
        indexed.sort(key=lambda x: -x[0])

        # Step 3: Take top k values
        top_k = indexed[:k]

        # Step 4: Sort by original index to preserve order
        top_k.sort(key=lambda x: x[1])

        # Step 5: Extract the values
        return [val for val, _ in top_k]