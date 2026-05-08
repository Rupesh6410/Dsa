from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestending=nums[0]
        ans=nums[0]
        for i in range(1 ,len(nums)):
            a=bestending+nums[i]
            b=nums[i]
            bestending=max(a,b)
            ans=max(ans , bestending)
        return ans
