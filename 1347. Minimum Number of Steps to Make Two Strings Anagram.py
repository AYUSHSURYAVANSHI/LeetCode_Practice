<<<<<<< HEAD
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        # Calculate the absolute difference between counts and sum them
        total_steps = sum((count_s - count_t).values())

=======
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        # Calculate the absolute difference between counts and sum them
        total_steps = sum((count_s - count_t).values())

>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return total_steps