class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        def can_finish(k):
            hours = 0
            for p in piles:
                hours+=ceil(p/k)
            return hours<=h
            
        while low<=high:
            mid = (low+high)//2

            if can_finish(mid):
                high = mid -1
            else:
                low = mid +1
        return low

                    
