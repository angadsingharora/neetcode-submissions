class Solution:
    def jump(self, nums: List[int]) -> int:
        #start from beginning, jump the furthest, try it until it fails, jump second furthest
        #start from end, jump furthest back, seconf durthest back etc


        res = 0
        l = r = 0


        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            res += 1

        return res