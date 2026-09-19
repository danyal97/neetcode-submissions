class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}

        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i] = 1
        
        a = []
        d = sorted(d.items(),key = lambda x:x[1], reverse=True)
        # print(d)
        for i in range(k):
            a.append(d[i][0])
        #     if d[i]>=k:
        #         a.append(i)
        return a

        