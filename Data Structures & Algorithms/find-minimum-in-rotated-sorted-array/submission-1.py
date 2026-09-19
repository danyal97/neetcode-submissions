class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]
        else:
            while nums[r-1] < nums[r]:
                r-=1
            return nums[r]
        