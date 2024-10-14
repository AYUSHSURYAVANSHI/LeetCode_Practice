class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1

        for _ in range(n):
            result.append(current)
            current = self.get_next_number(current, n)

        return result

    def get_next_number(self, current: int, n: int) -> int:
        if current * 10 <= n:
            return current * 10  # Move to the next "level" in the lexicographical order

        if current >= n:
            current //= 10  # Go back to the parent node

        current += 1  # Increment to get to the next number
        
        while current % 10 == 0:
            current //= 10  # Remove trailing zeros

        return current