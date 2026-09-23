class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        myHeap = []

        for x,y in points:
            hyp = math.sqrt(x**2 + y**2)
            heapq.heappush(myHeap, (hyp, x, y))

        res = []

        for i in range(k):
            hyp, x, y = heapq.heappop(myHeap)
            res.append([x, y])

        return res