class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        goal = len(nums) - 1
        i = goal
        dp[goal] = True
        while i>0:
            if nums[i-1] + (i-1) >= goal:
                goal = i - 1
                dp[goal] = True
            i-=1
        return dp[0]

        