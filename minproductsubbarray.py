class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        minend=nums[0]
        maxend=nums[0]
        for i in range (1,len(nums)):
            a=nums[i]
            b=minend*nums[i]
            c=maxend*nums[i]
            maxend=max(a,max(b,c))
            minend=min(a,min(b,c))
            res=max(res,max(minend, maxend))
        return res
        