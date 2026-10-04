class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        mx = nums[0]
        sm = 0 
        while r < len(nums):
            sm += nums[r]
            mx = max(sm,mx)
            while sm < 0 and l<=r:
                sm= sm - nums[l]
                l+=1
            r+=1
        return mx
        