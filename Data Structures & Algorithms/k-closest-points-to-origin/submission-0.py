class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[]
        k_closest=[]
        for point in points :
            x,y=point
            distance.append((math.sqrt(x*x +y*y),point))
        heapq.heapify(distance)
        for _ in range(k):
            if len(distance) <1:
                return 
            point=heapq.heappop(distance)
            k_closest.append(point[1])
        return k_closest