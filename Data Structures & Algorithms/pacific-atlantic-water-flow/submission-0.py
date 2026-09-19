class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pc = []
        ac = []
        ans = []

        for r in range(len(heights)):
            for c  in range(0, len(heights[0])):
                if r == 0 or c == 0:
                    pc.append([r,c])
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    ac.append([r,c])
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                

                # chr = r
                # chc = c

                q = [[r,c]]
                check_pc = False
                check_ac = False
                visited = [[0 for vc in range(len(heights[0])) ] for vr in range(len(heights))  ]

                # print(r,c)

                while len(q):
                    # print(q)
                    chr, chc = q.pop()
                    
                    visited[chr][chc] = 1

                    if [chr,chc] in pc:
                        check_pc = True
                    
                    if [chr,chc] in ac:
                        check_ac = True

                    # print(chr,chc,q)
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for dr, dc in directions:
                        # print()
                        nr,nc = chr + dr, chc + dc
                        # print(str(chr)+ " " + str(chc)+ " " + str(nr) + " "+ str(nc))
                        if 0<=nr<len(heights) and 0<=nc<len(heights[0]):
                            
                            # print(0<=nr<len(heights))
                            # print(0<=nc<len(heights[0]))
                            # print(heights[chr][chc] >= heights[nr][nc])
                            # print(visited[nr][nc] == 0)
                            if heights[chr][chc] >= heights[nr][nc] and visited[nr][nc] == 0:
                                q.append([nr,nc])

                    # print(chr,chc,q)

                    if check_ac and check_pc:
                        ans.append([r,c])
                        break

        return(ans)

        