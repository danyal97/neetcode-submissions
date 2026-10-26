class Solution:
    def canJump(self, nums: List[int]) -> bool:
        d = {}
        def rec(index, ans):

           

            if index >= len(nums) - 1:
                return True
            
            d[index] = ans 

            for i in range(index, index + nums[index]):
                if i+1 not in d:
                    ans = rec(i+1, ans)
            
            return ans
        
        return (rec(0, False))

        