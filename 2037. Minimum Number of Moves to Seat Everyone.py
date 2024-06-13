class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort the seats array
        seats.sort()
        # Sort the students array
        students.sort()
        # Initialize the count of moves to 0
        count = 0       
        # Iterate through the sorted arrays
        for seat, student in zip(seats, students):
            # Calculate the absolute difference between the seat and student positions
            count += abs(seat - student)
        # Return the total count of moves
        return count