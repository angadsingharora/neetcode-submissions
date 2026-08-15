class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #hash table, key is number itself, value is longest consecutive sequence
        h = set(nums)
        l = []
        long = 0
        for i in range(len(nums)):
            if nums[i]-1 not in h:
                length = 0
                while (nums[i]+length) in h:
                    length+=1
                long = max(long, length)
        return long

            

        

