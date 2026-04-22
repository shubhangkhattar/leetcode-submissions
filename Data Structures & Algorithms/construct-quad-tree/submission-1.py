"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def isUnique (val,t,b,l,r):

            for i in range(t,b+1):
                for j in range(l,r+1):
                    if val == grid[i][j]:
                        continue
                    return False

            return True

        def createQuadTree(t,b,l,r):
            val = grid[t][l]

            if isUnique(val,t,b,l,r):
                return Node(val,True,None,None,None,None)
            
            cur = Node(val,False,None,None,None,None)
            cur.topLeft = createQuadTree(t,(t+b)//2,l,(l+r)//2)
            cur.topRight = createQuadTree(t,(t+b)//2,((l+r)//2)+1,r)
            cur.bottomLeft = createQuadTree(((t+b)//2)+1,b,l,(l+r)//2)
            cur.bottomRight = createQuadTree(((t+b)//2)+1,b,((l+r)//2)+1,r)

            return cur
        
        return createQuadTree(0,len(grid)-1,0,len(grid[0])-1)
            










                        