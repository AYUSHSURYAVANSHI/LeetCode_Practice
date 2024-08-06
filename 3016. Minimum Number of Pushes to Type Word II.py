class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each character
        frequency_map = Counter(word)

        # Create a max heap based on character frequency
        max_heap = [(-freq, char) for char, freq in frequency_map.items()]
        heapq.heapify(max_heap)

        count = 0
        j = 1
        
        # Calculate minimum pushes based on character priority
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            freq = -freq  # Convert back to positive frequency
            
            if j <= 8:
                count += freq
            elif j <= 16:
                count += freq * 2
            elif j <= 24:
                count += freq * 3
            else:
                count += freq * 4
            
            j += 1
        
        return count