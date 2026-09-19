class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        d = {}
        st = set(nums)
        lrg = 0
        for i in nums:
            k = i
            if k-1 not in st:
                l = 1
                while (k + 1) in st:
                    l+=1
                    k = k +1
                lrg = max(l,lrg)
        return lrg

        