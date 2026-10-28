class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        jump = 0
        i = len(nums) - 1
        i_g = goal
        while i > 0:   
            while i >= 0:  
                if nums[i] + i >= goal:
                    i_g = i
                i = i - 1
            i = i_g
            goal = i_g
            jump+=1
        return jump