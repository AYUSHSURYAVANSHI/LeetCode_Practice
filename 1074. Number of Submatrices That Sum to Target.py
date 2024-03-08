<<<<<<< HEAD
class Solution:
    def numSubmatrixSumTarget(self, A: List[List[int]], target: int) -> int:
        # Get the dimensions of the matrix
        m, n = len(A), len(A[0])

        # Compute the cumulative sum for each row
        for row in A:
            for i in range(n - 1):
                row[i + 1] += row[i]

        res = 0  # Initialize the result variable to count submatrices

        # Iterate over all possible pairs of columns
        for i in range(n):
            for j in range(i, n):
                c = collections.defaultdict(int)
                cur, c[0] = 0, 1  # Initialize the current sum and a counter for cumulative sums

                # Iterate over each row to calculate the submatrix sum
                for k in range(m):
                    # Update the current sum based on the cumulative row sums
                    cur += A[k][j] - (A[k][i - 1] if i > 0 else 0)

                    # Count submatrices with the target sum using cumulative sums
                    res += c[cur - target]

                    # Update the counter for the current cumulative sum
                    c[cur] += 1

=======
class Solution:
    def numSubmatrixSumTarget(self, A: List[List[int]], target: int) -> int:
        # Get the dimensions of the matrix
        m, n = len(A), len(A[0])

        # Compute the cumulative sum for each row
        for row in A:
            for i in range(n - 1):
                row[i + 1] += row[i]

        res = 0  # Initialize the result variable to count submatrices

        # Iterate over all possible pairs of columns
        for i in range(n):
            for j in range(i, n):
                c = collections.defaultdict(int)
                cur, c[0] = 0, 1  # Initialize the current sum and a counter for cumulative sums

                # Iterate over each row to calculate the submatrix sum
                for k in range(m):
                    # Update the current sum based on the cumulative row sums
                    cur += A[k][j] - (A[k][i - 1] if i > 0 else 0)

                    # Count submatrices with the target sum using cumulative sums
                    res += c[cur - target]

                    # Update the counter for the current cumulative sum
                    c[cur] += 1

>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return res