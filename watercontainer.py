from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
      
        l=0
        n=len(height)
        r=n-1
        maxarea=-10**18
        while l<r:
            min_height=min(height[l] , height[r])
            length=r-l
            maxarea=max(maxarea , min_height*length)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxarea
        