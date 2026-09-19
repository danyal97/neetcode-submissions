class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ky = set()
        for i in range(0,len(nums)):
            k = nums[i] * -1
            d = {}
            for j in range(i+1,len(nums)):
                
                if (k - nums[j]) in d.keys():
                    # print([nums[i],  nums[j], d[k - nums[j]]])
                    asf = tuple(sorted([nums[i],  nums[j], d[k - nums[j]]]))
                    ky.add(asf)
                d[nums[j]] = nums[j]
        return [list(i) for i in ky]
        # print(ky)