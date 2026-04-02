class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_possibility(k):
            total=0
            for bananas in piles:
                total+=math.ceil(bananas/k)
            return total<=h

        n=len(piles)
        if h<n:
            return -1
        maxi=max(piles)
        i=1
        j=maxi
        while i<j:
            mid=i+(j-i)//2
            can_finish=check_possibility(mid)
            if can_finish:
                j=mid
            else:
                i=mid+1
            
            
        return i