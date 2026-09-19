class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [nums[0]]
        ln = len(nums)
        r = [nums[ln-1]]
        for i in range(1,len(nums)):
            l.append(l[i-1]*nums[i])
            r.append(r[i-1] * nums[ln-i-1])
        
        ans = []
        k = 0
        # print(l,r)
        for i in range(1,len(l)+1):
            if i == 2:
                ans.append(r[ln-i])
            elif i > 2:
                ans.append(r[ln-i]*l[k])
                k+=1
        ans.append(l[k])
        return ans

        