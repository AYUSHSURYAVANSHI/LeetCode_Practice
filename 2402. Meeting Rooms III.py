class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Step 1: Sort meetings by start time
        meetings.sort()

        # Step 2: Min-heap for available rooms (lowest room number)
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)

        # Step 3: Min-heap for busy rooms: (end time, room number)
        busy = []
        count = [0] * n  # Step 4: Count meetings per room

        # Step 5: Process each meeting
        for start, end in meetings:
            duration = end - start

            # Free rooms that have finished by current meeting start time
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                # Assign meeting to the smallest free room
                room = heapq.heappop(free_rooms)
                count[room] += 1
                heapq.heappush(busy, (end, room))
            else:
                # Delay the meeting until a room is free
                free_time, room = heapq.heappop(busy)
                count[room] += 1
                heapq.heappush(busy, (free_time + duration, room))

        # Step 6: Find room with most meetings
        max_meetings = max(count)
        for i, c in enumerate(count):
            if c == max_meetings:
                return i