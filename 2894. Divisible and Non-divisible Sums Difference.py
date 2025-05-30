class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        divisible_count = n // m
        divisible_sum = m * divisible_count * (divisible_count + 1) // 2
        return total_sum - 2 * divisible_sum