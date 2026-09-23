class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #convert to ascii or whatever assigned numerical value to each letter
        
        count = {}

        for task in tasks:
            if task not in count:
                count[task] = 1
            else:
                count[task] += 1

        maxHeap = []

        for cnt in count.values():
            maxHeap.append(-cnt)

        heapq.heapify(maxHeap)


        time = 0
        q = deque()

        while maxHeap or q:
            time +=1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
            
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time 