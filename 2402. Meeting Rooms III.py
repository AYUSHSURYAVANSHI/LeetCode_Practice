class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busy = [] # minHeap (end, room)
        avialable = [i for i in range(n)] # minHeap (room)
        count = [0] * n # count of how many times room was used

        meetings.sort() # sort meeting on start time => O(NlogN)

        # process each meeting => O(N)
        for start, end in meetings:
            # heap processing O(logN)
            # free the rooms, that were ended before current meeting start time
            while busy and busy[0][0] <= start:
                _end, room = heappop(busy)
                heappush(avialable, room)
            # if room is available take that, else take first free room from busy
            if avialable:
                room = heappop(avialable)
                heappush(busy, (end, room))
            else:
                _end, room = heappop(busy)
                heappush(busy, (end + (_end-start), room))
            # increment the count of room used
            count[room] += 1
        # return index of room that was use maximum number of times => O(N)
        return count.index(max(count))
        ## Time: O(NlogN) and Space: O(N), where n is the number of meetings