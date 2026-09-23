class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        myHeap = nums

        while len(myHeap) > k:
            heapq.heappop(myHeap)
        
        return heapq.heappop(myHeap)