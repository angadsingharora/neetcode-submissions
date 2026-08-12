class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashtable key is number itself and valye is times it appears. return number which has max occurences

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        freq = []

        for i in range(len(nums) + 1):
            freq.append([])

        for n in count:
            frequency = count[n]
            freq[frequency].append(n)

        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)

                if len(result) == k:
                    return result