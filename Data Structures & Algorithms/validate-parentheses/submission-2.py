class Solution:
    def isValid(self, s: str) -> bool:

        arra = []
        # print(f[0:len(f)-1])
        d = {"(": "(", "[": "[", "{": "{"}

        for i in s:
            if len(arra)>=1 and ((i == "}" and arra[-1] == "{") or (i == "]" and arra[-1] == "[" ) or (i == ")" and arra[-1] == "(")):
                arra.pop(-1)
            else:
                arra.append(i)
        
        # print(arra)
        return len(arra) == 0
        