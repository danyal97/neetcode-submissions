class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def rec(arr):

            if len(arr) == 0:
                return [[]]
            
            first = arr[0]
            rest = rec(arr[1:])
            ans = []
            # print(rest,first)
            for i in rest:
                d = i.copy()
                d.append(first)
                ans.append(d)
            
            # print(rest+ans)
            return ans + rest 
        return(rec(nums))



        