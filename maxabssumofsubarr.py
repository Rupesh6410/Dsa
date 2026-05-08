class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res=abs(nums[0])
        maxsum=nums[0]
        minsum=nums[0]
        for i in range(1,len(nums)):
            a=nums[i]
            b=nums[i]+maxsum
            c=nums[i]+minsum

            maxsum=max(a,b)
            minsum=min(a,c)
            res=(max(res , abs(minsum), maxsum))
        return res
        