class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i in range(0,len(nums)):
            k = target - nums[i]
            if k in d.keys():
                return [d[k],i]
            d[nums[i]] = i
        return []
        


        