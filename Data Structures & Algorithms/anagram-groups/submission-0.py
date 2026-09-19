class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        output = []
        for i in strs:
            k = "".join(sorted(i))
            if k in d.keys():
                d[k].append(i)
            else:
                d[k] = [i]
        
        for i in d:
            output.append(d[i])
        
        return output
        