class Solution:
    # def get_dist(x,y):
    #     return math.sqrt(x**2 + y**2) 
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_dist(x,y):
            return math.sqrt(x**2 + y**2) 
        min_heap = []
        n = len(points)
        for i in range(n):
            x = points[i][0]
            y = points[i][1]

            heappush(min_heap,(get_dist(x,y),points[i]))
        result = []
        for i in range(k):
            result.append(heappop(min_heap)[1])
        return result
        
