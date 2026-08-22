class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find which way its rotated... imagine it is [2,3,4,5,6,1]...m = 4
        res = nums[0]                                    #[5,6,1,2,3,4]...m = 1
        left = 0
        right = len(nums) - 1

        while left<=right:
            mid= (left+right)//2
            if nums[left]< nums[right]:
                res = min(res, nums[left])
                break
            res = min(res,nums[mid])
            if nums[mid]>=nums[left]:
                left = mid+1
            else:
                right= mid-1
        return res
