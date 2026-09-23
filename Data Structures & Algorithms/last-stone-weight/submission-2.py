class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #max heap
        #compare index 1 and index 2. compare that with index 0. run conditions. return last stone

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        myHeap = stones

        while len(myHeap) > 1:
            x = heapq.heappop(myHeap)
            y = heapq.heappop(myHeap)
            

            x, y = -1*x, -1*y

            if y < x: 
                heapq.heappush(myHeap, -(x-y))
           
        if myHeap:
            return -1*myHeap[0]
        return 0

