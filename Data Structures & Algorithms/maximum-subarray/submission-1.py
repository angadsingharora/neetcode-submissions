class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        best = nums[0]

        for i in range(1,len(nums)):
            if current + nums[i] > nums[i]:
                current = current + nums[i]
                
            else:
                current = nums[i]

            best = max(best, current)

        return best