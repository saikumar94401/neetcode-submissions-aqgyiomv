class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def pickStones(i,j,p1,p2,alice):
            if i>j:
                return p1>p2
            
            temp=False
            if alice:
                temp =temp or pickStones(i+1,j,p1+piles[i],p2,not alice)
                temp=temp or pickStones(i,j-1,p1+piles[j],p2,not alice)
            else:
                temp =temp or pickStones(i+1,j,p1,p2+piles[i],not alice)
                temp=temp or pickStones(i,j-1,p1,p2+piles[j],not alice)

            return temp





        return pickStones(0,len(piles)-1,0,0,True)